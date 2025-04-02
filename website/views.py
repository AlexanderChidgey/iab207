from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    events = [
        {
            'name': 'Coldplay Music of the Spheres',
            'photo': 'static/images/coldplay.jpg',
            'description': 'A spectacular music event featuring Coldplay and their latest album "Music of the Spheres".',
            'status': 'Open'
        },
        {
            'name': 'Sandtunes',
            'photo': 'static/images/sandtunes.jpg',
            'description': 'An exciting open-air event with performances by local and international artists.',
            'status': 'Open'
        },
        {
            'name': 'Carnaval',
            'photo': 'static/images/carnaval.avif',
            'description': 'Join us for a fun-filled Carnaval with music, dance, and vibrant celebrations.',
            'status': 'Open'
        },
        {
            'name': 'Coldplay Music of the Spheres',
            'photo': 'static/images/coldplay.jpg',
            'description': 'A spectacular music event featuring Coldplay and their latest album "Music of the Spheres".',
            'status': 'Open'
        },
        {
            'name': 'Sandtunes',
            'photo': 'static/images/sandtunes.jpg',
            'description': 'An exciting open-air event with performances by local and international artists.',
            'status': 'Open'
        },
        {
            'name': 'Carnaval',
            'photo': 'static/images/carnaval.avif',
            'description': 'Join us for a fun-filled Carnaval with music, dance, and vibrant celebrations.',
            'status': 'Open'
        },
        {
            'name': 'Carnaval',
            'photo': 'static/images/carnaval.avif',
            'description': 'Join us for a fun-filled Carnaval with music, dance, and vibrant celebrations.',
            'status': 'Open'
        }
    ]
    return render_template('main.html', events=events)

@main_bp.route("/event")
def home():
    return render_template('event.html')