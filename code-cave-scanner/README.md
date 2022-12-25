# Code Cave Scanner

### CLI tool to scan binaries for [Code Caves](https://en.wikipedia.org/wiki/Code_cave)


<img width="762" alt="Screenshot 2022-12-25 at 02 53 44" src="https://user-images.githubusercontent.com/24588573/209455102-221befac-e967-4b22-9876-3ac9b7cae937.png">

## About this project

Once again I fell in love with game hacking and decided to take everything a step further this time.  
Using [code caves](https://en.wikipedia.org/wiki/Code_cave) you can inject your custom [ASM code](https://en.wikipedia.org/wiki/Assembly_language) into almost any executable.
Since code caves are usally just "empty" parts within a file (e.g. 0x0 bytes) I decided to write a little script to help me find a fitting cave.

Also for this project I decided to pair-program with ChatGPT. I wanted to try it for quite some time now and what can I say. I am just blown away!  
I literally didn't use any other resource than ChatGPT when questions about Python popped up or when I just couldn't find the reason for a small bug.

# Usage

`python main.py path_to_program.exe 300` where 300 is the size in bytes the code cave should have.


## Todo

- Error handling
- Multi-threading
- More colors!

## Resources

- [ChatGPT](https://openai.com/blog/chatgpt/)
