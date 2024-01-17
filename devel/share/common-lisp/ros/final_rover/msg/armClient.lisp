; Auto-generated. Do not edit!


(cl:in-package final_rover-msg)


;//! \htmlinclude armClient.msg.html

(cl:defclass <armClient> (roslisp-msg-protocol:ros-message)
  ((y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (command
    :reader command
    :initarg :command
    :type cl:integer
    :initform 0)
   (position
    :reader position
    :initarg :position
    :type cl:fixnum
    :initform 0)
   (pitch
    :reader pitch
    :initarg :pitch
    :type cl:float
    :initform 0.0)
   (yaw
    :reader yaw
    :initarg :yaw
    :type cl:float
    :initform 0.0)
   (gripper
    :reader gripper
    :initarg :gripper
    :type cl:fixnum
    :initform 0))
)

(cl:defclass armClient (<armClient>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <armClient>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'armClient)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name final_rover-msg:<armClient> is deprecated: use final_rover-msg:armClient instead.")))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <armClient>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader final_rover-msg:y-val is deprecated.  Use final_rover-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'command-val :lambda-list '(m))
(cl:defmethod command-val ((m <armClient>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader final_rover-msg:command-val is deprecated.  Use final_rover-msg:command instead.")
  (command m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <armClient>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader final_rover-msg:position-val is deprecated.  Use final_rover-msg:position instead.")
  (position m))

(cl:ensure-generic-function 'pitch-val :lambda-list '(m))
(cl:defmethod pitch-val ((m <armClient>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader final_rover-msg:pitch-val is deprecated.  Use final_rover-msg:pitch instead.")
  (pitch m))

(cl:ensure-generic-function 'yaw-val :lambda-list '(m))
(cl:defmethod yaw-val ((m <armClient>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader final_rover-msg:yaw-val is deprecated.  Use final_rover-msg:yaw instead.")
  (yaw m))

(cl:ensure-generic-function 'gripper-val :lambda-list '(m))
(cl:defmethod gripper-val ((m <armClient>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader final_rover-msg:gripper-val is deprecated.  Use final_rover-msg:gripper instead.")
  (gripper m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <armClient>) ostream)
  "Serializes a message object of type '<armClient>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'command)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'position)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'pitch))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'yaw))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'gripper)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <armClient>) istream)
  "Deserializes a message object of type '<armClient>"
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
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'command)) (cl:read-byte istream))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'position) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pitch) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yaw) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gripper) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<armClient>)))
  "Returns string type for a message object of type '<armClient>"
  "final_rover/armClient")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'armClient)))
  "Returns string type for a message object of type 'armClient"
  "final_rover/armClient")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<armClient>)))
  "Returns md5sum for a message object of type '<armClient>"
  "6475c3b95c87883ceb5174259fc15e38")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'armClient)))
  "Returns md5sum for a message object of type 'armClient"
  "6475c3b95c87883ceb5174259fc15e38")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<armClient>)))
  "Returns full string definition for message of type '<armClient>"
  (cl:format cl:nil "float64 y~%char command~%int16 position~%float64 pitch~%float64 yaw~%int16 gripper~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'armClient)))
  "Returns full string definition for message of type 'armClient"
  (cl:format cl:nil "float64 y~%char command~%int16 position~%float64 pitch~%float64 yaw~%int16 gripper~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <armClient>))
  (cl:+ 0
     8
     1
     2
     8
     8
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <armClient>))
  "Converts a ROS message object to a list"
  (cl:list 'armClient
    (cl:cons ':y (y msg))
    (cl:cons ':command (command msg))
    (cl:cons ':position (position msg))
    (cl:cons ':pitch (pitch msg))
    (cl:cons ':yaw (yaw msg))
    (cl:cons ':gripper (gripper msg))
))
