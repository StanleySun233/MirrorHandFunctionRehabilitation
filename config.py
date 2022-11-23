DatabasePath = './data.db'

GlobalPath = "D:/SoftwareData/pycharm/MirrorHandFunctionRehabilitation/"
MinioPath = '47.100.93.63'
MinioPort = '9000'
MinioAccount = 'minioadmin'
MinioPassword = 'minioadmin'
MinioBucket = 'mhfr'

ConsoleIp = '127.0.0.1'
ConsolePort = '5000'

InternetIp = '127.0.0.1'
InternetSecurity = False
InternetAddress = 'http{}://{}:{}'.format('s' if InternetSecurity else '', InternetIp, ConsolePort)

LeftCaptureId = 0
RightCaptureId = 1
# RightCaptureId = 'rtsp://admin:@192.168.2.100:554/stream1'

UserInfoTable = 'user'

userLogin = '{}/{}/{}'.format(InternetAddress, UserInfoTable, 'login')
userRegister = '{}/{}/{}'.format(InternetAddress, UserInfoTable, 'register')
userForget = '{}/{}/{}'.format(InternetAddress, UserInfoTable, 'forget')
userGetAccountById = '{}/{}/{}'.format(InternetAddress, UserInfoTable, 'getAccountById')

PatientInfoTable = 'patient'

patientEasyList = '{}/{}/{}'.format(InternetAddress, PatientInfoTable, 'easyList')
patientListByName = '{}/{}/{}'.format(InternetAddress, PatientInfoTable, 'listByName')
patientListByDetail = '{}/{}/{}'.format(InternetAddress, PatientInfoTable, 'listByDetail')
patientGetById = '{}/{}/{}'.format(InternetAddress, PatientInfoTable, 'getById')
patientInsert = '{}/{}/{}'.format(InternetAddress, PatientInfoTable, 'insert')
patientUpdateById = '{}/{}/{}'.format(InternetAddress, PatientInfoTable, 'updateById')

TrainInfoTable = 'trainInfo'
trainInfoListByDate = '{}/{}/{}'.format(InternetAddress, TrainInfoTable, 'listByDate')
trainInfoInsert = '{}/{}/{}'.format(InternetAddress, TrainInfoTable, 'insert')
trainInfoListByIdAndTrain = '{}/{}/{}'.format(InternetAddress, TrainInfoTable, 'listByIdAndTrain')

Minio = 'file'
fileUpload = '{}/{}/{}'.format(InternetAddress, Minio, 'upload')
fileDownload = '{}/{}/{}'.format(InternetAddress, Minio, 'download')

SpaceImageConfigTable = 'spaceImageConfig'
spaceImageConfigList = '{}/{}/{}'.format(InternetAddress, SpaceImageConfigTable, 'list')
spaceImageConfigInsert = '{}/{}/{}'.format(InternetAddress, SpaceImageConfigTable, 'insert')
spaceImageConfigGetPic = '{}/{}/{}'.format(InternetAddress, SpaceImageConfigTable, 'getPic')
spaceImageConfigGetById = '{}/{}/{}'.format(InternetAddress, SpaceImageConfigTable, 'getById')

ashworthTable = 'ashworth'
ashworthInsert = '{}/{}/{}'.format(InternetAddress, ashworthTable, 'insert')

muscleStrengthTable = 'muscleStrength'
muscleStrengthInsert = '{}/{}/{}'.format(InternetAddress, muscleStrengthTable, 'insert')

VASTable = 'vas'
VASInsert = '{}/{}/{}'.format(InternetAddress, VASTable, 'insert')

addPlanTable = 'addPlan'
addPlanInsert = '{}/{}/{}'.format(InternetAddress, addPlanTable, 'insert')