/* 结构，在这里只是为了方便描述，实际使用时传参可以直接传列表而不单独定义对象 */
/* 设备 */
struct Device{
    int device_id
    str name
    str type
    float parameter
    date date_buy
    float price
    str manufactor
    int warranty_period
    str bought_by
    str manager_user
    str state
}
/* 审批查询_教师 */
struct Ask{
    int device_id
    str user_student
    str user_teacher
}

/* LoginInterface Class */
/*
    方法：init()
    描述：登录界面的mainloop
    输入：无
    外部输入：
        1、用户名
        2、密码
    输出：无
    返回：无
    协作类：Login、TeacherInterface、StudentInterface
*/
init(){
    while(loop){
        if(click(登录)){ // 按下“登录”按键
            if(Login.loginVerify(input.user, input.password, input type)){ // 密码正确
                if(input.type == "Teacher")
                    TeacherInterface.openWindow(input.user)
                else if(input.type == "Student")
                    StudentInterface.openWindow(input.user)
            }
            else{
                msgbox("No such account or password incorrect!")
            }
        }
        if(click(close)) // 退出
            system.close()
    }
}

/* Login Class */
/*
    方法：loginVerify(str user, str password, str type)
    描述：尝试进行登录操作，若成功，返回true，否则返回false
    输入：
        1、用户账号
        2、用户密码
        3、用户类型
    外部输入：无
    输出：无
    返回：登录是否成功
    协作类：LoginInterface、DB
*/
loginVerify(str user, str password, str type){
    if(type == "Teacher"){
        sql = "select user
        from teacher
        where (user == %s) and
        (password == %s);" % (user, password)
        result = executeSQL(sql)
        if(length(result) == 0)
            return false
        else
            return true
    }
    else if(type == "Student"){
        sql = "select user
        from student
        where (user == %s) and
        (password == %s);" % (user, password)
        result = executeSQL(sql)
        if(length(result) == 0)
            return false
        else
            return true
    }
    else{
        return false
    }
}

/* TeacherInterface Class */
/*
    方法：openWindow(str user)
    描述：教师图形界面的mainloop
    输入：用户账号
    外部输入：无
    输出：无
    返回：无
    协作类：LoginInterface、AddDevInterface、FixDevInterface、ApprovalInterface、TeacherQueryDevInterface    
*/
openWindow(str user){
    self.user = user
    while(loop){
        if(click(添加设备))
            AddDevInterface.openWindow(self.user)
        if(click(维修/报废设备))
            FixDevInterface.openWindow(self.user)
        if(click(申请审批))
            ApprovalInterface.openWindow(self.user)
        if(click(我管理的设备))
            TeacherQueryDevInterface.openWindow(self.user)
        if(click(close))
            system.close()
    }
}

/* StudentInterface Class */
/*
    方法：openWindow(str user)
    描述：学生图形界面的mainloop
    输入：用户账号
    外部输入：无
    输出：无
    返回：无
    协作类：LoginInterface、StudentQueryDevInterface、StudentQueryAskInterface
*/
openWindow(str user){
    self.user = user
    while(loop){
        if(click(设备查询))
            AddDevInterface.openWindow(self.user)
        if(click(我的申请))
            FixDevInterface.openWindow(self.user)
        if(click(close))
            system.close()
    }
}

/* AddDevInterface Class */
/*
    方法：openWindow(str user)
    描述：教师添加设备界面的mainloop
    输入：用户账号
    外部输入：仪器的各种信息
    输出：无
    返回：无
    协作类：TeacherInterface、AddDev
*/
openWindow(str user){
    self.user = user
    while(loop){
        if(click(添加)){ // 输入信息后确认添加
            if(Device中除了state外的任何一个属性未被指定)
                msgbox("Please enter full info!")
            else{
                Device.state = "空闲"
                if(AddDev.addDevReq(input.Device))
                    msgbox("Success!")
                else
                    msgbox("Fail!")
            }
        }
        if(click(close))
            system.close()
    }
}

/* FixDevInterface Class */
/*
    方法：openWindow(str user)
    描述：教师维修/报废界面的mainloop
    输入：用户账号
    外部输入：
        1、仪器id
        2、维修/报废原因
    输出：无
    返回：无
    协作类：TeacherInterface、FixDev
*/
openWindow(str user){
    self.user = user
    self.mode = 0 // 默认0表示维修，1表示报废
    while(loop){
        if(click(维修)) // 维修选项
            self.mode = 0
        if(click(报废)) // 报废选项
            self.mode = 1
        if(click(确认)){ // 输入信息后确认维修/报废
            if(id未被指定)
                msgbox("Please enter device id!")
            else{                
                if(FixDev.fixDevReq(input.user, input.devId, self.mode, date(), input.reason))
                    msgbox("Success!")
                else
                    msgbox("Fail!")
            }
        }
        if(click(close))
            system.close()
    }
}

/* ApprovalInterface Class */
/*
    方法：openWindow(str user)
    描述：教师审批界面的mainloop
    输入：用户账号
    外部输入：申请的各种筛选条件
    输出：无
    返回：无
    协作类：TeacherInterface、Approval、TeacherQueryAsk
*/
openWindow(str user){
    self.user = user
    for eachX in input.Ask中除user_teacher外的所有属性{ // 初始化界面时，筛选所有信息
        input.Ask.eachX = "*"
    }
    input.Ask.user_teacher = self.user
    TeacherQueryAsk.queryAskReq(input.Ask)
    while(loop){
        if(click(查询)){ // 按条件查询
            for eachX in input.Ask中的所有属性{ // 默认没有筛选条件
                if(eachX为空)
                    input.Ask.eachX = "*"
            }
            D = TeacherQueryAsk.queryAskReq(input.Ask)
            update(table, D) // 刷新查询结果
        }
        if(click(同意)){ // 申请通过
            if(Approval.approvalReq(select.user_student, select.devId, true))
                msgbox("Success!")
            else
                msgbox("Fail!")
        }
        if(click(拒绝)){ // 申请不通过
            if(Approval.approvalReq(select.user_student, select.devId, false))
                msgbox("Success!")
            else
                msgbox("Fail!")
        }
        if(click(close))
            system.close()
    }
}

/* TeacherQueryDevInterface Class */
/*
    方法：openWindow(str user)
    描述：教师查询设备界面的mainloop
    输入：用户账号
    外部输入：设备筛选条件
    输出：无
    返回：无
    协作类：TeacherInterface、TeacherQueryDev
*/
openWindow(str user){
    self.user = user
    Device.manager_user = self.user // 初始化Device的筛选条件
    其余筛选条件全部默认为"*"
    TeacherQueryDev.queryAskReq(input.Device)
    while(loop){
        if(click(查询)){ // 按条件查询
            for eachX in input.Device中的所有属性{ // 默认没有筛选条件
                if(eachX为空)
                    input.Device.eachX = "*"
            }
            D = TeacherQueryDev.queryAskReq(input.Device)
            update(table, D) // 刷新查询结果
        }
        if(click(close))
            system.close()
    }
}

/* StudentQueryDevInterface Class */
/*
    方法：openWindow(str user)
    描述：学生查询设备界面的mainloop
    输入：用户账号
    外部输入：
        1、设备筛选条件
        2、借用天数
    输出：无
    返回：无
    协作类：StudentInterface、StudentQueryDev、AskDev
*/
openWindow(str user){
    self.user = user
    筛选条件全部默认为"*"
    StudentQueryDev.queryAskReq(input.Device)
    while(loop){
        if(click(查询)){ // 按条件查询
            for eachX in input.Device中的所有属性{ // 默认没有筛选条件
                if(eachX为空)
                    input.Device.eachX = "*"
            }
            StudentQueryDev.queryAskReq(input.Device)
            update(table) // 刷新查询结果
        }
        if(click(申请)){ // 申请使用仪器
            if(AskDev.askDevReq(self.user, select.devId, input.days))
                msgbox("Success!")
            else
                msgbox("Fail!")
        }
        if(click(close))
            system.close()
    }
}

/* StudentQueryAskInterface Class */
/*
    方法：openWindow(str user)
    描述：学生查询申请界面的mainloop
    输入：用户账号
    外部输入：设备id
    输出：无
    返回：无
    协作类：StudentInterface、StudentQueryAsk、ReleaseDev
*/
openWindow(str user){
    self.user = user
    筛选条件全部默认为"*"
    StudentQueryAsk.queryAskReq(self.user, input.devId)
    while(loop){
        if(click(查询)){ // 按条件查询
            for eachX in input{ // 默认没有筛选条件
                if(eachX为空)
                    input.eachX = "*"
            }
            D = StudentQueryAsk.queryAskReq(self.user, input.devId)
            update(table, D) // 刷新查询结果
        }
        if(click(释放)){ // 释放仪器
            if(AskDev.releaseDevReq(select.devId))
                msgbox("Success!")
            else
                msgbox("Fail!")
        }
        if(click(close))
            system.close()
    }
}

/* AddDev Class */
/*
    方法：addDevReq(Device newDev)
    描述：尝试向数据库中添加设备
    输入：设备信息
    外部输入：无
    输出：无
    返回：添加是否成功
    协作类：AddDevInterface、DB
*/
addDevReq(Device newDev){
    addSql = "insert into device (id, name, type, parameter,
    date_buy, price, manufactor, warranty_period, bought_by,
    manager_user, state) value (%s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s)" % (Device.device_id, newDev.name,
    newDev.type, newDev.parameter, newDev.date_buy,
    newDev.price, newDev.manufactor, newDev.warranty_period,
    newDev.bought_by, newDev.manager_user, newDev.state)
    try{
        executeSQL(addSql)
        return true
    }
    except{
        return false
    }
}

/* FixDev Class */
/*
    方法：fixDevReq(str user, int devId, int mode, Date date, str reason)
    描述：更改数据库中的仪器的状态为维修/报废
    输入：
        1、教师用户名
        2、设备id
        3、报修模式（0：维修，1：报废）
        4、报修日期
    外部输入：无
    输出：无
    返回：修改数据库是否成功
    协作类：FixDevInterface、DB
*/
fixDevReq(str user, int devId, int mode, Date date, str reason){
    if(mode == 0){
        fixMode = "维修"
    }
    else if(mode == 1){
        fixMode = "报废"
    }
    orgState = executeSQL("select state from device where id = %s" % devId) // 如果原来的状态已经是维修或报废，则无法再报修一次
    if(orgState == "维修" or orgState == "报废")
        return false
    deviceSql = "update device set state = '%s' where id = %s" % (fixMode, mode)
    fixRecordSql = "insert into fix_record value(%s, %s, %s, %s)
    " % (user, devId, date, reason)
    try{
        executeSQL(deviceSql)
        executeSQL(fixRecordSql)
        return true
    }
    except{
        return false
    }
}

/* Approval Class */
/*
    方法：approvalReq(str user, int devId, boolean op)
    描述：审批请求，同意或拒绝。将相应更改写入到数据库
    输入：
        1、学生用户名
        2、设备id
        3、审核结果
    外部输入：无
    输出：无
    返回：审批操作是否成功
    协作类：ApprovalInterface、DB
*/
approvalReq(str user, int devId, boolean op){
    if(op == false){ // 拒绝
        try{
            executeSQL("update ask_record set is_pass = 'N' where student_user = %s and device_id = %s" % (user, devId))
            return true
        }
        except{
            return false
        }
    }
    else if(op == true){ // 同意
        agreeSql = "update ask_record set is_pass = 'Y' where student_user = %s and device_id = %s" % (user, devId) // 修改相应的请求记录为同意
        rejectSql = "update ask_record set is_pass = 'N' where student_user <> %s and device_id = %s and is_pass = 'P'" % (user, devId) // 拒绝其他人对这个设备的请求
        updateStateSql = "update device set state = '使用中' where student_user = %s and device_id = %s" % (user, devId) // 更新设备使用状态
        try{
            executeSQL(agreeSql)
            executeSQL(rejectSql)
            executeSQL(updateStateSql)
            return true
        }
        except{
            return false
        }
    }
}

/* TeacherQueryAsk Class */
/*
    方法：queryAskReq(Ask a)
    描述：教师查询学生的申请记录，根据条件，筛选并打印查询结果
    输入：查询申请时所输入的筛选条件
    外部输入：无
    输出：无
    返回：查询结果
    协作类：ApprovalInterface、DB
*/
queryAskReq(Ask a){
    // 设备id
    if(a.device_id == '*')
        querySqlDeviceIdPart = ""
    else
        querySqlDeviceIdPart = "ask_record.id = %s" % a.device_id
    // 学生账号
    if(a.user_student == '*')
        querySqlUserStudentPart = ""
    else
        querySqlUserStudentPart = "ask_record.user = %s" % a.user_student
    querySql = "select ask_record.user, ask_record.id, ask_record.date_ask, ask_record.days
    from (ask_record join device) where %s and %s and device.manager_user = %s
    and ask_record.id = device.id and is_pass = 'P'" % (querySqlDeviceIdPart, querySqlUserStudentPart, a.user_teacher) // 只选出待处理的进行显示
    D = executeSQL(querySql)
    return D
}

/* TeacherQueryDev Class */
/*
    方法：queryDevReq(Device dev)
    描述：教师查询自己管理的仪器情况，根据条件，筛选并打印查询结果
    输入：查询设备时所输入的筛选条件
    外部输入：无
    输出：无
    返回：查询结果
    协作类：TeacherQueryDevInterface、DB
*/
queryDevReq(Device dev){
    // 设备id
    if(dev.device_id == '*')
        querySqlDeviceIdPart = ""
    else
        querySqlDeviceIdPart = "id = %s" % dev.device_id
    // 设备名称
    if(dev.name == '*')
        querySqlNamePart = ""
    else
        querySqlNamePart = "name = %s" % dev.name
    // 设备类型
    if(dev.type == '*')
        querySqlTypePart = ""
    else
        querySqlTypePart = "type = %s" % dev.type
    // 设备参数
    if(dev.parameter == '*')
        querySqlParameterPart = ""
    else
        querySqlParameterPart = "parameter = %s" % dev.parameter
    // 购买日期
    if(dev.date_buy == '*')
        querySqlDateBuyPart = ""
    else
        querySqlDateBuyPart = "date_buy = %s" % dev.date_buy
    // 价格
    if(dev.price == '*')
        querySqlPricePart = ""
    else
        querySqlPricePart = "price = %s" % dev.price
    // 生产厂家
    if(dev.manufactor == '*')
        querySqlManufactorPart = ""
    else
        querySqlManufactorPart = "manufactor = %s" % dev.manufactor
    // 保修期
    if(dev.warranty_period == '*')
        querySqlWPPart = ""
    else
        querySqlWPPart = "warranty_period = %s" % dev.warranty_period
    // 购买人
    if(dev.bought_by == '*')
        querySqlBBPart = ""
    else
        querySqlBBPart = "bought_by = %s" % dev.bought_by
    // 设备状态
    if(dev.state == '*')
        querySqlStatePart = ""
    else
        querySqlStatePart = "state = %s" % dev.state

    // 管理者
    querySqlMUPart = "manager_user = %s" % dev.manager_user

    querySql = "select * from device where %s and %s and %s
    and %s and %s and %s and %s and %s and %s and %s and %s
    " % (querySqlDeviceIdPart, querySqlNamePart, querySqlTypePart,
        querySqlParameterPart, querySqlDateBuyPart, querySqlPricePart,
        querySqlManufactorPart, querySqlWPPart, querySqlBBPart,
        querySqlStatePart, querySqlMUPart)
    D = executeSQL(querySql)
    return D
}

/* StudentQueryDev Class */
/*
    方法：queryDevReq(Device dev)
    描述：学生查询自己全部仪器情况，根据条件，筛选并打印查询结果
    输入：查询设备时所输入的筛选条件
    外部输入：无
    输出：无
    返回：查询结果
    协作类：StudentQueryDevInterface、DB
*/
queryDevReq(Device dev){
    // 设备id
    if(dev.device_id == '*')
        querySqlDeviceIdPart = ""
    else
        querySqlDeviceIdPart = "id = %s" % dev.device_id
    // 设备名称
    if(dev.name == '*')
        querySqlNamePart = ""
    else
        querySqlNamePart = "name = %s" % dev.name
    // 设备类型
    if(dev.type == '*')
        querySqlTypePart = ""
    else
        querySqlTypePart = "type = %s" % dev.type
    // 设备参数
    if(dev.parameter == '*')
        querySqlParameterPart = ""
    else
        querySqlParameterPart = "parameter = %s" % dev.parameter
    // 购买日期
    if(dev.date_buy == '*')
        querySqlDateBuyPart = ""
    else
        querySqlDateBuyPart = "date_buy = %s" % dev.date_buy
    // 价格
    if(dev.price == '*')
        querySqlPricePart = ""
    else
        querySqlPricePart = "price = %s" % dev.price
    // 生产厂家
    if(dev.manufactor == '*')
        querySqlManufactorPart = ""
    else
        querySqlManufactorPart = "manufactor = %s" % dev.manufactor
    // 保修期
    if(dev.warranty_period == '*')
        querySqlWPPart = ""
    else
        querySqlWPPart = "warranty_period = %s" % dev.warranty_period
    // 购买人
    if(dev.bought_by == '*')
        querySqlBBPart = ""
    else
        querySqlBBPart = "bought_by = %s" % dev.bought_by
    // 管理者
    if(dev.manager_user == '*')
        querySqlMUPart = ""
    else
        querySqlMUPart = "manager_user = %s" % dev.manager_user
    // 设备状态
    if(dev.state == '*')
        querySqlStatePart = ""
    else
        querySqlStatePart = "state = %s" % dev.state


    querySql = "select * from device where %s and %s and %s
    and %s and %s and %s and %s and %s and %s and %s and %s
    " % (querySqlDeviceIdPart, querySqlNamePart, querySqlTypePart,
        querySqlParameterPart, querySqlDateBuyPart, querySqlPricePart,
        querySqlManufactorPart, querySqlWPPart, querySqlBBPart,
        querySqlStatePart, querySqlMUPart)
    D = executeSQL(querySql)
    return D
}

/* AskDev Class */
/*
    方法：askDevReq(str user, int devId, int days)
    描述：处理学生申请设备的请求
    输入：
        1、学生用户名
        2、设备id
        3、申请使用天数
    外部输入：无
    输出：无
    返回：申请是否有效
    协作类：StudentQueryDevInterface、DB
*/
askDevReq(str user, int devId, int days){
    // 设备状态必须为'空闲'才可以申请
    state = executeSQL("select state from device where id = %s" % str(devId))
    if(state == '空闲'){
        addAskRecordSql = "insert into ask_record(id, user, date_ask, days) values(%s, %s, %s, %s)" % (devId, user, date(), str(days)) // 增加一条申请
        try{
            executeSQL(addAskRecordSql)
            return true
        }
        except{
            return false
        }
    }
    else
        return false
}

/* StudentQueryAsk Class */
/*
    方法：queryAskReq(str user, int devId, str state)
    描述：学生查询的申请记录，根据条件，筛选并打印查询结果
    输入：
        1、学生账号
        2、设备id
    外部输入：无
    输出：无
    返回：查询结果
    协作类：StudentQueryAskInterface、DB
*/
queryAskReq(str user, int devId){
    // 学生账号
    if(user == '*')
        querySqlUserPart = ""
    else
        querySqlUserPart = "ask_record.user = %s" % user
    // 设备id
    if(devId == '*')
        querySqlIdPart = ""
    else
        querySqlIdPart = "ask_record.id = %s" % str(id)
    
    querySql = "select ask_record.id, ask_record.date_ask, ask_record.days, ask_record.date_start, ask_record.is_pass
    from (ask_record join device) where %s and %s
    and ask_record.id = device.id" % (querySqlUserPart, querySqlIdPart) // 只选出待处理的进行显示
    D = executeSQL(querySql)
    return D
}

/* ReleaseDev Class */
/*
    方法：releaseDevReq(int devId)
    描述：学生释放设备，使设备状态回到"空闲"
    输入：设备id
    外部输入：无
    输出：无
    返回：释放是否成功
    协作类：StudentQueryAskInterface、DB
*/
releaseDevReq(int devId){
    releaseSql = "update device set state = '空闲' where id = %s" % str(devId)
    try{
        executeSQL(releaseSql)
        return true
    }
    except{
        return false
    }
}