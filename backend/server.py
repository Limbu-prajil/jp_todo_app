import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2
from psycopg2.extras import RealDictCursor

class TodoHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _get_db_connection(self):
        return psycopg2.connect(
            dbname="todo_db",
            user="postgres",
            password="PostgresLogin24#",
            host="localhost"
        )

    def _execute_query(self, query, params=None, fetch_one=False):
        with self._get_db_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                conn.commit()
                if query.strip().upper().startswith(('SELECT', 'INSERT', 'UPDATE')):  # Only fetch results for SELECT or INSERT or UPDATE queries
                    if fetch_one:
                        return cursor.fetchone()
                    else:
                        return cursor.fetchall()
                return None  # No results to fetch for DELETE

    def _serialize_todo(self, todo):
        if todo and 'created_at' in todo:
            todo['created_at'] = todo['created_at'].isoformat()
        return todo

    def do_OPTIONS(self):
        self._set_headers()

    def do_GET(self):
        if self.path == '/todos':
            todos = self._execute_query("SELECT * FROM todos")
            if todos:
                self._set_headers()
                self.wfile.write(json.dumps([self._serialize_todo(todo) for todo in todos]).encode())
            else:
                self._set_headers(500)
                self.wfile.write(json.dumps({"Terror": "No todos found."}).encode())

    def do_POST(self):
        if self.path == '/todos':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            new_todo = self._execute_query(
                "INSERT INTO todos (title) VALUES (%s) RETURNING id, title, created_at, completed",
                (data['title'],),
                fetch_one=True
            )
            if new_todo:
                self._set_headers()
                self.wfile.write(json.dumps(self._serialize_todo(new_todo)).encode())
            else:
                self._set_headers(500)
                self.wfile.write(json.dumps({"Terror": "Todo not added."}).encode())

    def do_PUT(self):
        if self.path.startswith('/todos/'):
            todo_id = self.path.split('/')[-1]    
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            data = json.loads(put_data)
            updated_todo = self._execute_query(
                "UPDATE todos SET completed = %s WHERE id = %s RETURNING id, title, created_at, completed",
                (data['completed'], todo_id),
                fetch_one=True
            )
            if updated_todo:
                self._set_headers()
                self.wfile.write(json.dumps(self._serialize_todo(updated_todo)).encode())
            else:
                self._set_headers(500)
                self.wfile.write(json.dumps({"Terror": "Todo not found."}).encode())

    def do_DELETE(self):
        if self.path.startswith('/todos/'):
            todo_id = self.path.split('/')[-1]
            self._execute_query("DELETE FROM todos WHERE id = %s", (todo_id,))
            self._set_headers(204)

def run(server_class=HTTPServer, handler_class=TodoHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
