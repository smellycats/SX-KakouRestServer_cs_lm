# -*- coding: utf-8 -*-
import json
from functools import wraps

import arrow
from flask import g, request, make_response, jsonify, abort
from flask_restful import reqparse, abort, Resource
from passlib.hash import sha256_crypt
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from . import db, app, api, auth, cache, logger, access_logger
from .models import *


@app.route('/')
def index_get():
    result = {
        'cltx_url': '%scltx' % (request.url_root)
    }
    header = {'Cache-Control': 'public, max-age=60, s-maxage=60'}
    return jsonify(result), 200, header


@app.route('/cltx/<string:id>', methods=['GET'])
def cltx_get(id):
    try:
        i = Illegal.query.filter_by(ID=id).first()
    except Exception as e:
        logger.exception(e)
        raise
    if i is None:
        abort(404)
    try:
        hphm = {'Na': '-'}
        item = {
	    'id': i.ID,
	    'hphm': hphm.get(i.VehicleNo, i.VehicleNo),
	    'jgsj': i.IllTime.strftime('%Y-%m-%d %H:%M:%S'),
            'hpys': app.config['HPYS_DICT'].get(i.VehicleColor, (9, 'QT', '其他'))[2],
            'hpys_id': app.config['HPYS_DICT'].get(i.VehicleColor, (9, 'QT', '其他'))[0],
            'hpys_code': app.config['HPYS_DICT'].get(i.VehicleColor, (9, 'QT', '其他'))[1],
	    'kkdd': app.config['KKDD_DICT'].get(i.CrossingNo, (None,''))[1],
	    'kkdd_id': app.config['KKDD_DICT'].get(i.CrossingNo, (None,''))[0],
            'fxbh': app.config['FXBH_DICT'].get(i.Direction, (0, '其他'))[1],
            'fxbh_id': app.config['FXBH_DICT'].get(i.Direction, (0, '其他'))[0],
            'cdbh': int(i.RoadWayNo),
            'clsd': int(i.VehicleSpeed),
            'clsx': int(i.LimitSpeed),
            'hpzl': '0',
            'kkbh': i.CrossingNo,
            'imgurl': '{0}{1}'.format(i.PicUrl.replace('\\', '/'), i.Pic1)
        }
        return jsonify(item), 200
    except Exception as e:
        logger.exception(e)
        raise


@app.route('/cltx', methods=['GET'])
def cltx_list_get():
    q = request.args.get('q', None)
    if q is None:
        abort(400)
    try:
        args = json.loads(q)
    except Exception as e:
        logger.error(e)
        abort(400)
    try:
        limit = int(args.get('per_page', 20))
        offset = (int(args.get('page', 1)) - 1) * limit
        query = db.session.query(Illegal)
        if args.get('st', None) is not None:
            query = query.filter(Illegal.IllTime >= arrow.get(args['st']).datetime.replace(tzinfo=None))
        if args.get('et', None) is not None:
            query = query.filter(Illegal.IllTime <= arrow.get(args['et']).datetime.replace(tzinfo=None))
        if args.get('hphm', None) is not None:
            query = query.filter(Illegal.VehicleNo == args['hphm'])
            if args.get('st', None) is None:
                query = query.filter(Illegal.IllTime >= arrow.now('PRC').replace(days=-1).datetime.replace(tzinfo=None))
        result = query.limit(limit).offset(offset).all()

	# 结果集为空
        if len(result) == 0:
            return jsonify({'total_count': 0, 'items': []}), 200
        # 总数
        total = query.count()
	# 结果集第一个元素是否有缓存
        hphm = {'Na': '-'}
        items = []
        for i in result:
            item = {
	        'id': i.ID,
	        'hphm': hphm.get(i.VehicleNo, i.VehicleNo),
	        'jgsj': i.IllTime.strftime('%Y-%m-%d %H:%M:%S'),
                'hpys': app.config['HPYS_DICT'].get(i.VehicleColor, (9, 'QT', '其他'))[2],
                'hpys_id': app.config['HPYS_DICT'].get(i.VehicleColor, (9, 'QT', '其他'))[0],
                'hpys_code': app.config['HPYS_DICT'].get(i.VehicleColor, (9, 'QT', '其他'))[1],
	        'kkdd': app.config['KKDD_DICT'].get(i.CrossingNo, (None,''))[1],
	        'kkdd_id': app.config['KKDD_DICT'].get(i.CrossingNo, (None,''))[0],
                'fxbh': app.config['FXBH_DICT'].get(i.Direction, (0, '其他'))[1],
                'fxbh_id': app.config['FXBH_DICT'].get(i.Direction, (0, '其他'))[0],
                'cdbh': int(i.RoadWayNo),
                'clsd': int(i.VehicleSpeed),
                'clsx': int(i.LimitSpeed),
                'hpzl': '0',
                'kkbh': i.CrossingNo,
                'imgurl': '{0}{1}'.format(i.PicUrl.replace('\\', '/'), i.Pic1)
            }
            items.append(item)
        return jsonify({'total_count': total, 'items': items}), 200
    except Exception as e:
        logger.exception(e)
        raise
