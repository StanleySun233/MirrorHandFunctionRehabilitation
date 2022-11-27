from flask import Flask, request

import backend.model
import backend.service
import config
import tool

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

sqliteClient = tool.SqliteHelper.SqliteHelper(config.DatabasePath)
sqliteClient.setConnection()

minioClient = tool.MinioHelper.MinioHelper(config.MinioPath,
                                           config.MinioPort,
                                           config.MinioAccount,
                                           config.MinioPassword,
                                           config.MinioBucket)
minioClient.setConnection()

userInfoModel = backend.model.UserInfo.UserInfo('user_info', sqliteClient)
patientInfoModel = backend.model.PatientInfo.PatientInfo('patient_info', sqliteClient)
trainInfoModel = backend.model.TrainInfo.TrainInfo('train_info', sqliteClient)
spaceImageConfigModel = backend.model.SpaceImageConfig.SpaceImageConfig('space_image_config', sqliteClient)
ashworthModel = backend.model.Ashworth.Ashworth('ashworth', sqliteClient)
muscleStrengthModel = backend.model.MuscleStrength.MuscleStrength('muscle_strength', sqliteClient)
VASModel = backend.model.VAS.VAS('vas', sqliteClient)
AddPlanModel = backend.model.AddPlan.AddPlan('add_plan', sqliteClient)

userInfoService = backend.service.UserInfoService.UserInfoService(userInfoModel)
patientInfoService = backend.service.PatientInfoService.PatientInfoService(patientInfoModel)
trainInfoService = backend.service.TrainInfoService.TrainInfoService(trainInfoModel)
spaceImageConfigService = backend.service.SpaceImageConfigService.SpaceImageConfigService(spaceImageConfigModel)
ashworthService = backend.service.Ashworth.AshworhService(ashworthModel)
muscleStrengthService = backend.service.MuscleStrength.MuscleStrength(muscleStrengthModel)
VASService = backend.service.VASService.VASService(VASModel)
addPlanService = backend.service.AddPlan.AddPlanService(VASModel)


@app.route('/file/upload', methods=['POST', 'GET'])
def fileUpload():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = minioClient.uploadFileByUrl(data['name'])
    return res


@app.route('/file/download', methods=['POST', 'GET'])
def fileDownload():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = minioClient.downloadFileByUrl(data['name'])
    return res


@app.route('/user/login', methods=['POST', 'GET'])
def userLogin():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = userInfoService.login(data)
    return res


@app.route('/user/register', methods=['POST', 'GET'])
def userRegister():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = userInfoService.register(data)
    return res


@app.route('/user/forget', methods=['POST', 'GET'])
def userForget():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = userInfoService.forget(data)
    return res


@app.route('/user/getAccountById', methods=['POST', 'GET'])
def userGetAccountById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = userInfoService.getAccountById(data)
    return res


@app.route('/patient/easyList', methods=['POST', 'GET'])
def patientList():
    res = patientInfoService.listByName()
    return res


@app.route('/patient/listByName', methods=['POST', 'GET'])
def patientListByName():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = patientInfoService.listByName(data)
    return res


@app.route('/patient/listByDetail', methods=['POST', 'GET'])
def patientListByDetail():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = patientInfoService.list(attrs=data)
    return res


@app.route('/patient/getById', methods=['POST', 'GET'])
def patientGetById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = patientInfoService.getById(data['id'])
    return res


@app.route('/patient/insert', methods=['POST', 'GET'])
def patientInsert():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = patientInfoService.insert(data)
    return res


@app.route('/patient/updateById', methods=['POST', 'GET'])
def patientUpdateById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    ids = data['id']
    del data['id']
    res = patientInfoService.updateById(ids, data)
    return res


@app.route('/trainInfo/listByDate', methods=['POST', 'GET'])
def trainInfoListByDate():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = trainInfoService.listByDate(data)
    return res


@app.route('/trainInfo/insert', methods=['POST', 'GET'])
def trainInfoInsert():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = trainInfoService.insert(data, receiveId=True)
    return res


@app.route('/trainInfo/listByIdAndTrain', methods=['POST', 'GET'])
def trainInfoListByIdAndTrain():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = trainInfoService.list(attrs=data)
    return res


@app.route('/spaceImageConfig/list', methods=['POST', 'GET'])
def spaceImageConfigList():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = spaceImageConfigService.list()
    return res


@app.route('/spaceImageConfig/insert', methods=['POST', 'GET'])
def spaceImageConfigInsert():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = spaceImageConfigService.insert(data)
    return res


@app.route('/spaceImageConfig/getPic', methods=['POST', 'GET'])
def spaceImageConfigGetPic():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = spaceImageConfigService.getPic(data)
    return res


@app.route('/spaceImageConfig/getById', methods=['POST', 'GET'])
def spaceImageConfiggetById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = spaceImageConfigService.getById(data)
    return res


@app.route('/ashworth/insert', methods=['POST', 'GET'])
def ashworthInsert():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = ashworthService.insert(data)
    return res


@app.route('/muscleStrength/insert', methods=['POST', 'GET'])
def muscleStrengthInsert():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = muscleStrengthService.insert(data)
    return res


@app.route('/VAS/insert', methods=['POST', 'GET'])
def VASInsert():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = VASService.insert(data)
    return res


@app.route('/addPlan/insert', methods=['POST', 'GET'])
def addPlanInsert():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = addPlanService.insert(data)
    return res


def run():
    app.run(host=config.ConsoleIp, port=config.ConsolePort, debug=False, threaded=True)


if __name__ == "__main__":
    run()
