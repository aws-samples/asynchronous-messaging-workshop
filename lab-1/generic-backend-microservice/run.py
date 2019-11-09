import logging
import web

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    web.app.run(debug=False, host='0.0.0.0', port=80)