from flask import Flask, render_template, request
from riot_api import get_encrypted_puuid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        summoner_name = request.form['summoner_name']
        region = 'na1'  # Change to desired region if needed

        # Fetch encryptedPUUID using the summoner name
        encrypted_puuid = get_encrypted_puuid(summoner_name, region)
        if not encrypted_puuid:
            return render_template('index.html', error="Summoner not found!")

        # Render the encryptedPUUID or other details in the template
        return render_template('index.html', puuid=encrypted_puuid)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
