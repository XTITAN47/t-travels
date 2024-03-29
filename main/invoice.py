from reportlab.pdfgen import canvas
#pip install reportlab

def genFlightInvoice(airtktid,user,flightno,fname,flightname,a,b,p,gst,total):
    c = canvas.Canvas(f'Flight{airtktid}.pdf',pagesize=(400,400))
    c.rect(50,78,340,200)
    c.drawString(160,300,'Titan Travels')
    c.drawString(100,260,'Ticket Number')
    c.drawString(250,260,airtktid)
    c.drawString(100,240,'UserID')
    c.drawString(250,240,user)
    c.drawString(100,220,'Flight Number')
    c.drawString(250,220,flightno)
    c.drawString(100,200,'Full Name')
    c.drawString(250,200,fname)
    c.drawString(100,180,'Flight Name')
    c.drawString(250,180,flightname)
    c.drawString(100,160,'Departure')
    c.drawString(250,160,a)
    c.drawString(100,140,'Destination')
    c.drawString(250,140,b)
    c.drawString(100,120,'Sub Total')
    c.drawString(250,120,p)
    c.drawString(100,100,'GST 18%')
    c.drawString(250,100,gst)
    c.drawString(100,80,'Total')
    c.drawString(250,80,total)
    c.setFont('Helvetica',40)
    c.setTitle('INVOICE')
    c.save()
    print('PDF Generated..')

def genBusInvoice(bustktid,user,busid,fname,a,b,p,gst,total):
    c = canvas.Canvas(f'BusTkt{bustktid}.pdf',pagesize=(400,400))
    c.rect(50,78,340,200)
    c.drawString(160,300,'Titan Travels')
    c.drawString(100,260,'Ticket Number')
    c.drawString(250,260,bustktid)
    c.drawString(100,240,'UserID')
    c.drawString(250,240,user)
    c.drawString(100,220,'BUS Number')
    c.drawString(250,220,busid)
    c.drawString(100,200,'Full Name')
    c.drawString(250,200,fname)
    c.drawString(100,180,'Departure')
    c.drawString(250,180,a)
    c.drawString(100,160,'Destination')
    c.drawString(250,160,b)
    c.drawString(100,140,'Sub Total')
    c.drawString(250,140,p)
    c.drawString(100,120,'GST 18%')
    c.drawString(250,120,gst)
    c.drawString(100,100,'Total')
    c.drawString(250,100,total)
    c.setFont('Helvetica',40)
    c.setTitle('INVOICE')
    c.save()
    print('PDF Generated..')

def genTrainInvoice(traintktid,user,trainno,fname,trainname,a,b,p,gst,total):
    c = canvas.Canvas(f'Train{traintktid}.pdf',pagesize=(400,400))
    c.rect(50,78,340,200)
    c.drawString(160,300,'Titan Travels')
    c.drawString(100,260,'Ticket Number')
    c.drawString(250,260,traintktid)
    c.drawString(100,240,'UserID')
    c.drawString(250,240,user)
    c.drawString(100,220,'Train Number')
    c.drawString(250,220,trainno)
    c.drawString(100,200,'Full Name')
    c.drawString(250,200,fname)
    c.drawString(100,180,'Train Name')
    c.drawString(250,180,trainname)
    c.drawString(100,160,'Departure')
    c.drawString(250,160,a)
    c.drawString(100,140,'Destination')
    c.drawString(250,140,b)
    c.drawString(100,120,'Sub Total')
    c.drawString(250,120,p)
    c.drawString(100,100,'GST 18%')
    c.drawString(250,100,gst)
    c.drawString(100,80,'Total')
    c.drawString(250,80,total)
    c.setFont('Helvetica',40)
    c.setTitle('INVOICE')
    c.save()
    print('PDF Generated..')

def genHotelInvoice(htltktid,user,hotelid,fname,hname,roomtype,CheckInDate,CheckOutDate,p,gst,total):
    c = canvas.Canvas(f'Hotel{htltktid}.pdf',pagesize=(400,400))
    c.rect(50,58,340,220)
    c.drawString(160,300,'Titan Travels')
    c.drawString(100,260,'Ticket Number')
    c.drawString(250,260,htltktid)
    c.drawString(100,240,'UserID')
    c.drawString(250,240,user)
    c.drawString(100,220,'Hotel Number')
    c.drawString(250,220,hotelid)
    c.drawString(100,200,'Full Name')
    c.drawString(250,200,fname)
    c.drawString(100,180,'Hotel Name')
    c.drawString(250,180,hname)
    c.drawString(100,160,'Room Type')
    c.drawString(250,160,roomtype)
    c.drawString(100,140,'Check In')
    c.drawString(250,140,CheckInDate)
    c.drawString(100,120,'Check Out')
    c.drawString(250,120,CheckOutDate)
    c.drawString(100,100,'Sub Total')
    c.drawString(250,100,p)
    c.drawString(100,80,'GST 18%')
    c.drawString(250,80,gst)
    c.drawString(100,60,'Total')
    c.drawString(250,60,total)
    c.setFont('Helvetica',40)
    c.setTitle('INVOICE')
    c.save()
    print('PDF Generated..')


if __name__ == '__main__':
    gst = 0.18 * 8000
    total = gst + 8000
    gst = str(gst)
    total = str(total)
    #genTrainInvoice('AR0','titan','1','VIMARSH THAKUR','Vistara','Mumbai','Delhi','8000',gst,total)
    #genHotelInvoice('HTL1','user','hotelid','fname','Taj Hotel, Mumbai','roomtype','CheckInDate','CheckOutDate','8000',gst,total)
