from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId

client = MongoClient("mongodb+srv://youtube:rFGgRMkqxRCFUTQx@cluster0.j8qaxxp.mongodb.net/ytmanager", tlsAllowInvalidCertificates = True)
# not a good idea to include id and password in code files
# tlsAllowInvalidCertificates = True not a good way to handle test


db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID : {video['_id']} , Name : {video['name']} , Time : {video['time']}")

def add_video(name , time):
    video_collection.insert_one({"name" : name , "time" : time})

def update_video(video_id, new_name, new_time):
    try:
        result = video_collection.update_one(
            {'_id': ObjectId(video_id)},
            {'$set': {'name': new_name, 'time': new_time}}
        )

        if result.matched_count == 0:
            print("No video found with this ID.")
        else:
            print("Video updated successfully!")

    except InvalidId:
        print("Invalid video ID format!")

        
def delete_video(video_id):
    try:
        result = video_collection.delete_one(
            {'_id': ObjectId(video_id)}
        )

        if result.deleted_count == 0:
            print("No video found with this ID.")
        else:
            print("Video deleted successfully!")

    except InvalidId:
        print("Invalid video ID format!")


def main():
    while True:
        print("\n youtube manager | choose an option ")
        print("1. List of all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("enter your choice : ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("enter the video name : ")
            time = input("enter the video time : ")
            add_video(name , time)
        elif choice == '3':
            video_id = input("enter the video id to update : ")
            name = input("enter the updated video name : ")
            time = input("enter the updated video time : ")
            update_video(video_id , name , time)
        elif choice == '4':
            video_id = input("enter the video id to delete : ")
            delete_video(video_id)
        elif choice == '5':
            break
        else :
            print("invalid choice")


if __name__ == '__main__':
    main()
