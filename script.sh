#!/bin/bash
echo "Cleaning the directory of images"
cd
cd Desktop/check-assignments/images
rm assignment1_now.jpeg
cd ..
cd script-check-assignments
echo "Running the node script to get the new image."
node index.js
mv assignment1_now.jpeg /home/rafael/Desktop/check-assignments/images
sleep 5s
cd ..
echo "Running the python script to make show the difference of the images."
python image_diff.py --first images/assignment1_original.jpeg --second images/assignment1_now.jpeg
sleep 5s
echo "Moving the result files to images folder"
mv *.png /home/rafael/Desktop/check-assignments/images

echo "end of the  script!..."
