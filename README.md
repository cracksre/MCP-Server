# MCP-Server

Demo a MCP Server

## Version

The current version of this demo is **0.1.0** (initial release).

## Step-by-step setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/cracksre/MCP-Server.git
   cd MCP-Server
   ```

2. **Create a Python virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate    # on Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**
   ```bash
   python math-server.py
   ```
   The server listens on the default MCP port and exposes example procedures.

5. **Use the client**
   ```bash
   python mcp_client.py
   ```
   This will invoke the `add` procedure defined in `add_example.py`.

6. **Testing and development**
   - Modify or extend `add_example.py` to add new functions.
   - Restart the server after making changes.


Feel free to explore and adapt the code for your own MCP integrations.
