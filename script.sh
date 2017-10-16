#!/bin/bash
# in oder to show the convert commando, you need to install imagemagick "sudo apt-get install imagemagick"
echo "########################################"
echo "Beggining the execution of the script..."
echo "########################################"
echo "Cleaning the directory of images"
cd
cd Desktop/check-assignments/images
rm assignment1_now.jpeg *.png
cd ..
cd script-check-assignments
echo "Running the node script to get the new image."
node index.js
mv assignment1_now.jpeg /home/rafael/Desktop/check-assignments/images
sleep 5s
cd ..
echo "Resizing the images before running the python script"
#convert ~/Desktop/check-assignments/images/assignment1_original.jpeg -resize 800x8370! -quality 100 ~/Desktop/check-assignments/images/assignment1_original.jpeg
convert ~/Desktop/check-assignments/images/assignment1_now.jpeg -resize 800x8370! -quality 100 ~/Desktop/check-assignments/images/assignment1_now.jpeg
sleep 10s
echo "Running the python script to show the difference of the images."
python image_diff.py --first images/assignment1_original.jpeg --second images/assignment1_now.jpeg
sleep 5s
echo "Moving the result files to images folder"
mv *.png /home/rafael/Desktop/check-assignments/images
echo "########################################"
echo "Ending the execution of the script..."
echo "########################################"
