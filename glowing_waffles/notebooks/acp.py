class ObserveACP:
    
    def __init__(self, name, date):
        
        from astropy.coordinates import SkyCoord
        from astropy.time import Time
        import datetime
    
        self.name = name
        self.start_time = str(datetime.datetime.today()).split()[1][:8]
        self.filters = []
        self.im_count = 1
        self.binning = 1
        
        coords = SkyCoord.from_name(name)

        self.ra = coords.ra.deg
        self.dec = coords.dec.deg
        
        #self.date = str(datetime.datetime.today()).split()[0]
        self.date = date
        
        
    def wait_until(self, time):
        self.start_time = time
        
        
    def add_filter(self, filt):
        
        if filt in self.filters:
            print("Filter", filt, "is already in list!")
        
        elif isinstance(filt, str):
            # do the string thing
            self.filters.append(filt)
        
        elif not isinstance(filt, str):
            try:
                # loop over elements in filt
                for i in filt:
                    if i in self.filters:
                        print("Filter", i, "is already in list")
                        
                    else:
                        self.filters.append(i)
                    
            except IndexError:
                raise ValueError('filt must be a non-string iterable')
                
        
    def rm_filter(self, filt):
        
        if filt not in self.filters:
            print("No filter", filt, "in list")
        
        elif isinstance(filt, str):
            self.filters.remove(filt)
            
        elif not isinstance(filt, str):
            try:
                for i in filt:
                    if i in self.filters:
                        
                        self.filters.remove(i)
                        
                    else:
                        print("No filter", filt, "in list")
            except IndexError:
                raise ValueError('filt must be a non-string iterable')
                
        
        
    def expose(self, num):
        self.exposure = num
        
        
    def count(self, num):
        self.im_count = num
        
    
    def repeat(self, num):
        self.repeats = num
        
    
    def write(self, title):
    
        scalar = len(self.filters)
        
        f = open(title, 'w')
    
        f.write("#waituntil 1, " +  str(self.startTime) + '\n')
        f.write("#repeat " + str(self.repeats) + '\n')
        
        count = scalar * (str(self.imCount) + ',')
        f.write("#count " + count + '\n')
        
        f.write("#filter ")
        for i in self.filters:
            f.write(i + ',')
        f.write('\n')
        
        interval = scalar * (str(self.exposure) + ',')
        f.write("#interval " + interval + '\n')
        
        binning = scalar * (str(self.binning) + ',')
        f.write("#binning " + binning + '\n')
        
        RA = str(self.ra)
        DEC = str(self.dec)
        f.write(self.name + '    ' + RA + '    ' + DEC + '\n' + '\n')
      