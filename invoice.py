from reportlab.pdfgen import canvas
#pip install reportlab

def genFlightInvoice(airtktid,user,flightno,fname,flightname,a,b,p,gst,total):
    c = canvas.Canvas(f'Flight{airtktid}.pdf',pagesize=(400,400))
    c.rect(50,78,300,200)
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

if __name__ == '__main__':
    gst = 0.18 * 8000
    total = gst + 8000
    gst = str(gst)
    total = str(total)
    genFlightInvoice('AR0','titan','1','Raju','Vistara','Mumbai','Delhi','8000',gst,total)
