# Code Cave Scanner

A command line tool to scan binaries for [Code caves](https://en.wikipedia.org/wiki/Code_cave) and find suitable locations to inject custom [ASM code](https://en.wikipedia.org/wiki/Assembly_language).

<img width="762" alt="Screenshot of code cave scanner in action" src="https://user-images.githubusercontent.com/24588573/209455547-2d3fe932-8e3b-4bef-9e6c-42f5030dceec.png">


## Features

- Scan any executable file for code caves of a specified size or larger
- Sort code caves by size, from largest to smallest
- Print the address and size of each code cave found


## Usage

> `python main.py path_to_program.exe 300`

Where `path_to_program.exe` is the path to the executable file you want to scan, and `300` is the minimum size in bytes that the code cave should have.

Note that this script searches for code caves within all sections of the binary, not just the executable section.


## Resources

For this project I decided to pair-program with ChatGPT. I wanted to try it for quite some time now and what can I say. I am just blown away!  
- [ChatGPT](https://openai.com/blog/chatgpt/) for providing helpful guidance and assistance during the development of this project.
