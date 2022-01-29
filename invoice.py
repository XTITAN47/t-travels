from reportlab.pdfgen import canvas

def gst18(a):
    b = 0.18 * a
    l = [str(b),str(b+a)]
    return l

def genInvoice(a,b):
    c = canvas.Canvas('Invoice.pdf',pagesize=(400,400))
    c.rect(50,120,300,160)
    c.drawString(160,300,'Titan Travels')
    c.drawString(100,260,'Name')
    c.drawString(250,260,a[1])
    c.drawString(100,240,'UserID')
    c.drawString(250,240,a[2])
    c.drawString(100,220,'Bill Number')
    c.drawString(250,220,a[3])

    c.drawString(100,200,'Sub Total')
    c.drawString(250,200,a[4])

    c.drawString(100,180,'GST 18%')
    c.drawString(250,180,b[0])

    c.drawString(100,160,'Total')
    c.drawString(250,160,b[1])


    c.setFont('Helvetica',40)
    c.setTitle('INVOICE')
    c.save()
    print('PDF Generated..')

if __name__ == '__main__':
    a = ['','Sanchit','1','213213','5525']
    b = gst18(int(a[4]))
    genInvoice(a,b)
