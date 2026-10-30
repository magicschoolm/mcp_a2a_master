from fastmcp import FastMCP
import subprocess

mcp = FastMCP("terminal_server")

@mcp.tool
def run_commands(command: str) -> str:
    """
    Run a terminal command and return its output.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            capture_output=True,
        )
        return result.stdout or result.stderr
    except subprocess.CalledProcessError as e:
        return e.stderr

if __name__ == "__main__":
    mcp.run()