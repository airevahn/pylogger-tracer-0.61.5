from flask import Flask
import logging

app = Flask(__name__)

@app.route('/')
def main():
  app.logger.error("This is using manual instrumentation, ddtrace 0.61.5")
  return "manual instrumentation using ddtrace 0.61.5."

if __name__ == '__main__':
  app.run(port=8081)