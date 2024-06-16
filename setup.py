from pathlib import Path
from setuptools import find_packages, setup

home_dir = Path(__file__).parent
path = home_dir / "README.md"
long_desc = path.read_text()

setup(
    name="spotify-check-duplicates",
    version="0.1.0",
    entry_points="""
        [console_scripts]
        spotify-check-duplicates=spotify_check_duplicates.main:main
    """,
    install_requires=[
        "spotipy>=2,<3",
    ],
    description="Check if there are duplicates in your library",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/leroyguillaume/spotify-check-duplicates",
    author="Guillaume Leroy",
    author_email="pro.guillaume.leroy@gmail.com",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
