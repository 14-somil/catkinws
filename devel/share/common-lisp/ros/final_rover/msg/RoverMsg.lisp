; Auto-generated. Do not edit!


(cl:in-package final_rover-msg)


;//! \htmlinclude RoverMsg.msg.html

(cl:defclass <RoverMsg> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (isPID
    :reader isPID
    :initarg :isPID
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass RoverMsg (<RoverMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RoverMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RoverMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name final_rover-msg:<RoverMsg> is deprecated: use final_rover-msg:RoverMsg instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <RoverMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader final_rover-msg:x-val is deprecated.  Use final_rover-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <RoverMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader final_rover-msg:y-val is deprecated.  Use final_rover-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'isPID-val :lambda-list '(m))
(cl:defmethod isPID-val ((m <RoverMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader final_rover-msg:isPID-val is deprecated.  Use final_rover-msg:isPID instead.")
  (isPID m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RoverMsg>) ostream)
  "Serializes a message object of type '<RoverMsg>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'isPID) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RoverMsg>) istream)
  "Deserializes a message object of type '<RoverMsg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:slot-value msg 'isPID) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RoverMsg>)))
  "Returns string type for a message object of type '<RoverMsg>"
  "final_rover/RoverMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RoverMsg)))
  "Returns string type for a message object of type 'RoverMsg"
  "final_rover/RoverMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RoverMsg>)))
  "Returns md5sum for a message object of type '<RoverMsg>"
  "dac2c668a77a0aca11621addd50fbbe9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RoverMsg)))
  "Returns md5sum for a message object of type 'RoverMsg"
  "dac2c668a77a0aca11621addd50fbbe9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RoverMsg>)))
  "Returns full string definition for message of type '<RoverMsg>"
  (cl:format cl:nil "float64 x~%float64 y~%bool isPID~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RoverMsg)))
  "Returns full string definition for message of type 'RoverMsg"
  (cl:format cl:nil "float64 x~%float64 y~%bool isPID~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RoverMsg>))
  (cl:+ 0
     8
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RoverMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'RoverMsg
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':isPID (isPID msg))
))
