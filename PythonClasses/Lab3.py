class Date:
    def __init__(self,day,month,year ):
        self.day= day
        self.month= month
        self.year= year

    def __str__(self):
        return 'day:'+ (self.day)+',month:'+ (self.month)+',year:'+(self.year)

class DateTime(Date):
    def __init__(self,day, month, year, hours, minutes, seconds):
        Date.__init__( self,day, month, year)
        self.hours= hours
        self.minutes= minutes
        self.seconds= seconds
    def __str__ (self):
        return super().__str__() +'--'+(self.hours)+':'+self.minutes+':'+(self.seconds)


def dateF(format):
    def p(*dateP):
        dateList=[]
        for i in dateP:
           date = i.split("-")
           if format == 'big':
            dateOb= Date(date[2], date[1], date[0])
            dateList.append(dateOb)
           elif  format =='middle':
               dateOb= Date(date[1], date[0], date[2])
               dateList.append(dateOb)
           elif format == 'little':
               dateObj= Date(date[0], date[1], date[2])
               dateList.append(dateObj)
        return dateList
    return p

   
             
                 








           
     
       
     
   
   
       






# Add your code here

# Please use the following names to recieve the corresponding functions as they return from the outer function calls
bigEndianParser = dateF('big' )
littleEndianParser = dateF('little')
middleEndianParser = dateF('middle')

# Testing
def test_DateObjectCreation():
    d = Date('1','3','2020')
    assert d.__str__() == 'day:1,month:3,year:2020'

def test_DateTimeObjectCreation():
    dt = DateTime('1','3','2020', '11','22','33')
    assert dt.__str__() == 'day:1,month:3,year:2020--11:22:33'


def testBigEndian1():
    parsedDates = bigEndianParser('2021-03-31')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
   
   
def testBigEndian3():
    parsedDates = bigEndianParser('2021-03-31','2020-04-5','2019-05-15')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    assert parsedDates[1].__str__() == 'day:5,month:04,year:2020'
    assert parsedDates[2].__str__() == 'day:15,month:05,year:2019'

def testLittelEndian1():
    parsedDates = littleEndianParser('31-03-2021')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
   
   
def testLittelEndian3():
    parsedDates = littleEndianParser('31-03-2021','5-04-2020','15-05-2019')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    assert parsedDates[1].__str__() == 'day:5,month:04,year:2020'
    assert parsedDates[2].__str__() == 'day:15,month:05,year:2019'

def testMiddleEndian1():
    parsedDates = middleEndianParser('03-31-2021')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
   
   
def testMiddleEndian3():
    parsedDates = middleEndianParser('03-31-2021','04-5-2020','05-15-2019')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    assert parsedDates[1].__str__() == 'day:5,month:04,year:2020'
    assert parsedDates[2].__str__() == 'day:15,month:05,year:2019'

