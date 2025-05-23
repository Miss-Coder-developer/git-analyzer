from setuptools import setup, find_packages

setup(
    name="git-analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gitpython>=3.1.0",
        "openai>=1.0.0",
        "python-dotenv>=0.19.0",
    ],
    entry_points={
        'console_scripts': [
            'git-analyzer=git_analyzer.cli:main',
        ],
    },
    author="",
    author_email="",
    description="A powerful tool for analyzing Git repositories using LLM-powered insights",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/git-analyzer/",
    project_urls={
        "Documentation": "https://pypi.org/project/git-analyzer/",
        "Source": "",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Version Control :: Git",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="git, analysis, repository, llm, openai, gpt",
    python_requires=">=3.7",
) 
