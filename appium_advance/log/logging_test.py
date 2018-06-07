import  logging
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO,filename='runlog.log',
                    format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')

logging.debug('debug info')
logging.info('hello 51zxw')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')