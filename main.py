from flask import Flask, jsonify
import apinasdata

app = Flask(__name__)

@app.route('/scrape_nasdaq')
def scrape_nasdaq_route():
    try:
        # Call the scrape_nasdaq function
        apinasdata.scrape_nasdaq()

        # Provide a success response
        return jsonify({'status': 'success', 'message': 'Scraping completed successfully'})
    except Exception as e:
        # Provide an error response if an exception occurs
        return jsonify({'status': 'error', 'message': str(e)})

def main():
    app.run(host='127.0.0.1', debug=True, port=5000, threaded=True)

if __name__ == '__main__':
    main()
