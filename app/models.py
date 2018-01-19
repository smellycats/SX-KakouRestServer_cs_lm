# -*- coding: utf-8 -*-
import arrow

from . import db


class Illegal(db.Model):
    """过车表"""
    __tablename__ = 'Illegal'

    ID = db.Column(db.Integer, primary_key=True)
    VehicleNo = db.Column(db.String(50), default='')
    CrossingNo = db.Column(db.String(10), default='')
    VehicleNoColor = db.Column(db.String(10), default='')
    VehicleNoImage = db.Column(db.String(255), default='')
    VideoUrl = db.Column(db.String(50), default='')
    VehicleColor = db.Column(db.String(10), default='')
    Pic1 = db.Column(db.String(255), default='')
    Pic2 = db.Column(db.String(255), default='')
    Pic3 = db.Column(db.String(255), default='')
    Pic4 = db.Column(db.String(255), default='')
    IllTime = db.Column(db.DateTime, default=arrow.now('PRC').datetime.replace(tzinfo=None))
    InputTime = db.Column(db.DateTime, default=arrow.now('PRC').datetime.replace(tzinfo=None))
    Direction = db.Column(db.String(10), default='')
    RoadWayNo = db.Column(db.String(3), default='')
    VehicleLength = db.Column(db.String(20), default='')
    VehicleNoType = db.Column(db.String(10), default='')
    VehicleType = db.Column(db.String(10), default='')
    VehicleSpeed = db.Column(db.Integer, default=0)
    LimitSpeed = db.Column(db.Integer, default=0)
    IllType = db.Column(db.String(8), default='')
    PicUrl = db.Column(db.String(100), default='')
    PicName = db.Column(db.String(50), default='')

    def __init__(self, VehicleNo='', CrossingNo='', VehicleNoColor='', VehicleNoImage='',
                 VideoUrl='', VehicleColor='', Pic1='', Pic2='', Pic3='', Pic4='',
                 IllTime='', InputTime='', Direction='', RoadWayNo='', VehicleLength='',
                 VehicleNoType='', VehicleType='', VehicleSpeed=0, LimitSpeed=0,
                 IllType='', PicUrl='', PicName=''):
        self.VehicleNo = VehicleNo
        self.CrossingNo = CrossingNo
        self.VehicleNoColor = VehicleNoColor
        self.VehicleNoImage = VehicleNoImage
        self.VideoUrl = VideoUrl
        self.VehicleColor = VehicleColor
        self.Pic1 = Pic1
        self.Pic2 = Pic2
        self.Pic3 = Pic3
        self.Pic4 = Pic4
        self.IllTime = Illtime
        self.InputTime = InputTime
        self.Direction = Direction
        self.RoadWayNo = RoadWayNo
        self.VehicleLength = VehicleLength
        self.VehicleNoType = VehicleNoType
        self.VehicleType = VehicleType
        self.VehicleSpeed = VehicleSpeed
        self.LimitSpeed = LimitSpeed
        self.IllType = IllType
        self.PicUrl = PicUrl
        self.PicName = PicName

    def __repr__(self):
        return '<Illegal %r>' % self.ID


