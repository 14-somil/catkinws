; Auto-generated. Do not edit!


(cl:in-package final_rover-msg)


;//! \htmlinclude encodersFeedback.msg.html

(cl:defclass <encodersFeedback> (roslisp-msg-protocol:ros-message)
  ((first
    :reader first
    :initarg :first
    :type cl:float
    :initform 0.0)
   (second
    :reader second
    :initarg :second
    :type cl:float
    :initform 0.0))
)

(cl:defclass encodersFeedback (<encodersFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <encodersFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'encodersFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name final_rover-msg:<encodersFeedback> is deprecated: use final_rover-msg:encodersFeedback instead.")))

(cl:ensure-generic-function 'first-val :lambda-list '(m))
(cl:defmethod first-val ((m <encodersFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader final_rover-msg:first-val is deprecated.  Use final_rover-msg:first instead.")
  (first m))

(cl:ensure-generic-function 'second-val :lambda-list '(m))
(cl:defmethod second-val ((m <encodersFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader final_rover-msg:second-val is deprecated.  Use final_rover-msg:second instead.")
  (second m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <encodersFeedback>) ostream)
  "Serializes a message object of type '<encodersFeedback>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'first))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'second))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <encodersFeedback>) istream)
  "Deserializes a message object of type '<encodersFeedback>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'first) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'second) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<encodersFeedback>)))
  "Returns string type for a message object of type '<encodersFeedback>"
  "final_rover/encodersFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'encodersFeedback)))
  "Returns string type for a message object of type 'encodersFeedback"
  "final_rover/encodersFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<encodersFeedback>)))
  "Returns md5sum for a message object of type '<encodersFeedback>"
  "c8951f7da38088f2e93267537583f4e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'encodersFeedback)))
  "Returns md5sum for a message object of type 'encodersFeedback"
  "c8951f7da38088f2e93267537583f4e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<encodersFeedback>)))
  "Returns full string definition for message of type '<encodersFeedback>"
  (cl:format cl:nil "float64 first~%float64 second~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'encodersFeedback)))
  "Returns full string definition for message of type 'encodersFeedback"
  (cl:format cl:nil "float64 first~%float64 second~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <encodersFeedback>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <encodersFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'encodersFeedback
    (cl:cons ':first (first msg))
    (cl:cons ':second (second msg))
))
