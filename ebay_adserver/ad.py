import time

class Ad(object):

    def __init__(self, ad_id, width, height, creative):
        self.ad_id = ad_id
        self.width = width
        self.height = height
        self.time = time.time()
        self.creative = creative
        self.impressions = 0
        self.clicks = 0
        self.served = 0
    
    def __str__(self):
        output = {
            'ad_id': self.ad_id,
            'width': self.width,
            'height': self.height,
            'creative': self.creative,
            'impressions': self.impressions,
            'clicks': self.clicks,
            'time': self.time,
        }
        return str(output)

    def toJson(self):
        output = {
            'ad_id': self.ad_id,
            'width': self.width,
            'height': self.height,
            'creative': self.creative,
            'impressions': self.impressions,
            'clicks': self.clicks,
            'time': self.time,
        }
        return output

    ### Getters ###

    def getAdId(self):
        return self.adid

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getCreative(self):
        return self.creative

    def getClicks(self):
        return self.clicks

    def getImpressions(self):
        return self.impressions

    def getCreateTime(self):
        return self.time


    ### Setters ###

    def setWidth(self, width):
        self.width = width
        return True

    def setHeight(self, height):
        self.height = height
        return True

    def setCreative(self, creative):
        self.creative = creative
        return True
    
    def incImpressions(self):
        self.impressions += 1
        return True

    def incClicks(self):
        self.clicks += 1
        return True

    def incServed(self):
        self.served += 1
        return True
