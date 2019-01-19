import os

start_dir = os.getcwd()

# mahimahi
os.system("sudo sysctl -w net.ipv4.ip_forward=1")
os.system("sudo add-apt-repository -y ppa:keithw/mahimahi")
os.system("sudo apt-get -y update")
os.system("sudo apt-get -y install mahimahi")

# apache server
os.system("sudo apt-get -y install apache2")

#os.system("sudo cp video_server/ /var/www/html")
os.system("sudo cp video_server/test.html /var/www/html")
os.system("sudo cp video_server/dash.all.min.js /var/www/html")
os.system("sudo cp -r video_server/*.m4s /var/www/html")
os.system("sudo cp video_server/output.mpd /var/www/html")
os.system("sudo mkdir /var/www/html/dash")
os.system("sudo cp -r video_server/dash/*.m4s /var/www/html/dash")
os.system("sudo cp video_server/dash/output.mpd /var/www/html/dash")


