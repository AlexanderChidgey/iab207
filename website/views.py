from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

events = [
        {
            'id':1,
            'name': 'Coldplay Music of the Spheres',
            'photo': 'images/coldplay.jpg',
            'description': 'A spectacular music event featuring Coldplay and their latest album "Music of the Spheres".',
            'status': 'Open',
            "eventLocation": "Brisbane",
            "eventDate": "",
            "eventTags": "",
            "eventCategory": "Country",
            "ticketsAvaliable": "",
            "performingArtists": [],
            "eventType": "",
            "eventStartTime": "",
            "eventEndTime": "",
            
        },
        {
            'id':2,
            'name': 'Sandtunes',
            'photo': 'images/sandtunes.jpg',
            'description': 'An exciting open-air event with performances by local and international artists.',
            "eventCategory": "Country",
            'status': 'Open'
        },
        {
            'id':3,
            'name': 'Carnaval',
            'photo': 'images/carnaval.avif',
            'description': 'Join us for a fun-filled Carnaval with music, dance, and vibrant celebrations.',
            "eventCategory": "Pop",

            'status': 'Open'
        },
        {
            'id':4,
            'name': 'Coldplay Music of the Spheres',
            'photo': 'images/coldplay.jpg',
            "eventCategory": "Pop",
            'description': 'A spectacular music event featuring Coldplay and their latest album "Music of the Spheres".',
            'status': 'Open'
        },
        {
            'id':5,
            'name': 'Sandtunes',
            'photo': 'images/sandtunes.jpg',
            "eventCategory": "Pop",
            'description': 'An exciting open-air event with performances by local and international artists.',
            'status': 'Open'
        },
        {
            'id':6,
            'name': 'Carnaval',
            'photo': 'images/carnaval.avif',
            "eventCategory": "Pop",
            'description': 'Join us for a fun-filled Carnaval with music, dance, and vibrant celebrations.',
            'status': 'Open'
        },
        {
            'id':7,
            'name': 'Carnaval',
            'photo': 'images/carnaval.avif',
            "eventCategory": "Pop",
            'description': 'Join us for a fun-filled Carnaval with music, dance, and vibrant celebrations.',
            'status': 'Open'
        }
    ]


@main_bp.route('/')
def index():
    return render_template('main.html', events=events)

@main_bp.route("/eventData", methods=["POST"])
def eventData():
    eventLocation = request.form["eventLocation"]
    eventCategory = request.form["eventCategory"]
    data = []
    
    
    for e in events:
        if (e["eventCategory"] == eventCategory):
            data.append(e)
    print("data",data)
        
    return render_template("eventsView.html", data = data)    
    
    
    
@main_bp.route("/event/<int:event_id>")
def event_detail(event_id):
    event = None

    # Use next() for efficient lookup
    for e in events:
        if e["id"] == event_id:
            event = e

    if event is None:
        return "Event not found"
    

    return render_template('event.html', events=event)

@main_bp.route("/create")
def create_event():
    return render_template('createEvent.html')
# @main_bp.route("/event/<int:event_id>")
# def event_details(event_id):
#     print(event_id)
#     event = None
#     for e in events:
#         if e['id'] == event_id:
#             print(e)
#             event = e
#     if event == None:
#         return "Event not found", 404
        
#     # event = next((e for e in events if e["id"] == event_id), None)
#     # print(event)
#     # if not event:
#     #     return "Event not found", 404
#     # print(event)
#     return render_template('event.html', event=event)