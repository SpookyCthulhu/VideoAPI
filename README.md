# VideoAPI

This is a video transfer server made using Django, SQLite, and a rest API. Currently built only to work within a LAN, but capable of transfering between devices.

# Overiew

The front facing API of this application consists primarily of a uploads and downloads page, where a user may upload files to, and download files form the database respectively. Uploading by url is not currently supported, but will be in a future update. For right now, the database is primarily intended to be used alongside a tool like postman, or through curl on the command line interface. This application is useful for transfering videos to and from devices within your home or workplace without the need for a more complicated setup or manual transfer.

# Instructions

Hosting:
  The service can be hosted by simply running this command in the project root folder:
    python manage.py runserver <ipv4_address>:<desired_port_number>

Uploading: 
  Videos can be uploaded by using postman, or by using the following command in curl:
    curl -X POST http://<ipv4>:<port>/videos/upload/ \
     -H "Content-Type: multipart/form-data" \
     -F "title=<a_choosen_title>" \
     -F "video_file=@/<path_to_file>/<file_name>"

Downloading:
  Videos can be downloaded by either visiting the web address ending with the desired video id:
    "http://<ipv4>:<port>/videos/download/<video_id>/
  OR videos can be downloaded in a similar way using Curl in the desired folder:
    curl -o <desired_file_name_w/type> http://<ipv4>:<port>/videos/download/<video_id>/

# License

You are free to use and modify any of the code in my work for your own projects!
