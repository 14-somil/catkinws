; Auto-generated. Do not edit!


(cl:in-package beginner_tutorials-msg)


;//! \htmlinclude anglesMsg.msg.html

(cl:defclass <anglesMsg> (roslisp-msg-protocol:ros-message)
  ((first
    :reader first
    :initarg :first
    :type cl:integer
    :initform 0)
   (second
    :reader second
    :initarg :second
    :type cl:integer
    :initform 0)
   (base
    :reader base
    :initarg :base
    :type cl:integer
    :initform 0)
   (servo1
    :reader servo1
    :initarg :servo1
    :type cl:integer
    :initform 0)
   (servo2
    :reader servo2
    :initarg :servo2
    :type cl:integer
    :initform 0)
   (isPump
    :reader isPump
    :initarg :isPump
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass anglesMsg (<anglesMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <anglesMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'anglesMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-msg:<anglesMsg> is deprecated: use beginner_tutorials-msg:anglesMsg instead.")))

(cl:ensure-generic-function 'first-val :lambda-list '(m))
(cl:defmethod first-val ((m <anglesMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:first-val is deprecated.  Use beginner_tutorials-msg:first instead.")
  (first m))

(cl:ensure-generic-function 'second-val :lambda-list '(m))
(cl:defmethod second-val ((m <anglesMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:second-val is deprecated.  Use beginner_tutorials-msg:second instead.")
  (second m))

(cl:ensure-generic-function 'base-val :lambda-list '(m))
(cl:defmethod base-val ((m <anglesMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:base-val is deprecated.  Use beginner_tutorials-msg:base instead.")
  (base m))

(cl:ensure-generic-function 'servo1-val :lambda-list '(m))
(cl:defmethod servo1-val ((m <anglesMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:servo1-val is deprecated.  Use beginner_tutorials-msg:servo1 instead.")
  (servo1 m))

(cl:ensure-generic-function 'servo2-val :lambda-list '(m))
(cl:defmethod servo2-val ((m <anglesMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:servo2-val is deprecated.  Use beginner_tutorials-msg:servo2 instead.")
  (servo2 m))

(cl:ensure-generic-function 'isPump-val :lambda-list '(m))
(cl:defmethod isPump-val ((m <anglesMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:isPump-val is deprecated.  Use beginner_tutorials-msg:isPump instead.")
  (isPump m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <anglesMsg>) ostream)
  "Serializes a message object of type '<anglesMsg>"
  (cl:let* ((signed (cl:slot-value msg 'first)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'second)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'base)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'servo1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'servo2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'isPump) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <anglesMsg>) istream)
  "Deserializes a message object of type '<anglesMsg>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'first) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'second) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'base)) (cl:read-byte istream))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo1) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo2) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:setf (cl:slot-value msg 'isPump) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<anglesMsg>)))
  "Returns string type for a message object of type '<anglesMsg>"
  "beginner_tutorials/anglesMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'anglesMsg)))
  "Returns string type for a message object of type 'anglesMsg"
  "beginner_tutorials/anglesMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<anglesMsg>)))
  "Returns md5sum for a message object of type '<anglesMsg>"
  "54456492e189535a538699a4d3569641")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'anglesMsg)))
  "Returns md5sum for a message object of type 'anglesMsg"
  "54456492e189535a538699a4d3569641")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<anglesMsg>)))
  "Returns full string definition for message of type '<anglesMsg>"
  (cl:format cl:nil "int64 first~%int64 second~%char base~%int64 servo1 ~%int64 servo2~%bool isPump~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'anglesMsg)))
  "Returns full string definition for message of type 'anglesMsg"
  (cl:format cl:nil "int64 first~%int64 second~%char base~%int64 servo1 ~%int64 servo2~%bool isPump~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <anglesMsg>))
  (cl:+ 0
     8
     8
     1
     8
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <anglesMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'anglesMsg
    (cl:cons ':first (first msg))
    (cl:cons ':second (second msg))
    (cl:cons ':base (base msg))
    (cl:cons ':servo1 (servo1 msg))
    (cl:cons ':servo2 (servo2 msg))
    (cl:cons ':isPump (isPump msg))
))