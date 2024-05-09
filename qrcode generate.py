import qrcode

#define the data 
data = 'https://www.youtube.com/'  
#create qrcode 
QRCodefile = "image.png" 
# Generating the QR code 
QRimage = qrcode.make(data) 
# Saving image into a file 
QRimage.save(QRCodefile) 
qrObject = qrcode.QRCode(version=1, box_size=12,border=10) 
# add data to the QR code 
qrObject.add_data(data) 
# compile the data into a QR code array 
qrObject.make() 
image = qrObject.make_image(fill_color="red") 
image.save(QRCodefile)