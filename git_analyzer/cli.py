from git import Repo, Git
import json
from datetime import datetime, timedelta
import os
import tempfile
import shutil
import openai
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from git_analyzer.core import (
    EnhancedGitAnalyzer,
    MilestoneDetector,
    CommitClusterer,
    TechnicalChallengeDetector,
    ImpactAnalyzer,
    ContributorAnalyzer
)
from git_analyzer.llm import LLMAnalyzer, ReportGenerator
import argparse

# Load environment variables from .env file
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description='Analyze a Git repository and generate a report.')
    parser.add_argument('repo_url', help='URL of the Git repository')
    parser.add_argument('--start-date', help='Start date for analysis (YYYY-MM-DD)')
    parser.add_argument('--end-date', help='End date for analysis (YYYY-MM-DD)')
    parser.add_argument('--output-dir', default='reports', help='Output directory for reports')
    parser.add_argument('--format', default='json', choices=['json', 'markdown'], help='Output format (json or markdown)')
    parser.add_argument('--openai-key', help='OpenAI API key')
    parser.add_argument('--custom-prompts', help='Path to custom prompts JSON file')
    parser.add_argument('--model', default='gpt-4o-mini', help='OpenAI model to use')
    
    args = parser.parse_args()
    
    # Initialize components
    with EnhancedGitAnalyzer(args.repo_url, args.start_date, args.end_date) as analyzer:
        # Extract commits
        commits = analyzer.extract_all_commits()
        
        # Initialize analyzers
        milestone_detector = MilestoneDetector()
        commit_clusterer = CommitClusterer()
        challenge_detector = TechnicalChallengeDetector()
        impact_analyzer = ImpactAnalyzer()
        contributor_analyzer = ContributorAnalyzer()
        
        # Run all analyses
        milestones = milestone_detector.detect_milestones(commits)
        clusters = commit_clusterer.cluster_commits(commits)
        challenges = challenge_detector.detect_challenges(commits)
        impact_data = impact_analyzer.analyze_impact(commits)
        contributor_data = contributor_analyzer.analyze_contributors(commits)
        
        # Create analysis report
        report = {
            "repository": analyzer.get_repository_name(),
            "generated_at": datetime.now().isoformat(),
            "analysis_period": {
                "start": args.start_date,
                "end": args.end_date
            },
            "total_commits": len(commits),
            "total_authors": len(set(c['author'] for c in commits)),
            "total_files_changed": len(set(f for c in commits for f in c['files_changed'])),
            "total_insertions": sum(c['insertions'] for c in commits),
            "total_deletions": sum(c['deletions'] for c in commits),
            "milestones": milestones,
            "commit_clusters": clusters,
            "technical_challenges": challenges,
            "impact_analysis": impact_data,
            "contributor_analysis": contributor_data,
            "commits": commits
        }
        
        # Perform LLM analysis
        llm_analyzer = LLMAnalyzer(
            api_key=args.openai_key,
            model=args.model,
            custom_prompts_path=args.custom_prompts
        )
        llm_analysis = llm_analyzer.analyze_repository(
            commits,
            milestones=milestones,
            challenges=challenges,
            contributor_data=contributor_data,
            impact_data=impact_data
        )
        report['llm_analysis'] = llm_analysis
        
        # Generate report
        report_generator = ReportGenerator(output_dir=args.output_dir)
        report_file = report_generator.generate_report(
            report,
            report['repository'],
            format=args.format
        )
        
        print(f"Report generated: {report_file}")

if __name__ == "__main__":
    main() 