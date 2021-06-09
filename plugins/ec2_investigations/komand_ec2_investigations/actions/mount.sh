#!/bin/bash

# Make is executable first: chmod +x ./mount.sh
# To run the script: ./mount.sh suspect_mount2 /dev/xvdf1

# Test if the first input (the directory you want the volume mount to) is valid 
if [ -d $1 ]
then 
	# Error 1 - Unable to mount. Directory already exisits.
	echo "1"
	exit 1		
else 
	errorline=$(mkdir $1 2>&1)
	length=${#errorline}
	if [ $length != 0 ]
	then
		# Error 2 - Invalid directory
		echo "2"
		exit 1
 	fi
fi

# Test if the second input (the directory of the volume) is vaild 
if [ ! -b $2 ]
then
	# Error 0 - Unable to mount. Device does not exist.
	echo "0"
	# Remove the directory we created in the first part so that the directory 
	# can be reused if the second part return error. 	
	rm -r $1
	exit 1
fi

# Test if the volume is successfully mounted
errorFormat=$(mount -o ro $2 $1 2>&1)
length1=${#errorFormat}
if [ $length1 != 0 ]
then
	errorMsg3="{\"directory\":\"$2\",\"status\":\"$errorFormat\"}"
	echo $errorMsg3
	# Remove the directory we created in the first part so that the directory 
	# can be reused if the third part return error. 	
	rm -r $1
	exit 1
else
	# Successfully mounted
	successMsg="{\"directory\":\"$1\",\"status\":\"Successfully mounted\"}"
	echo $successMsg
fi

