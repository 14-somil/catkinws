; Auto-generated. Do not edit!


(cl:in-package beginner_tutorials-msg)


;//! \htmlinclude example.msg.html

(cl:defclass <example> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type cl:float
    :initform 0.0))
)

(cl:defclass example (<example>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <example>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'example)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-msg:<example> is deprecated: use beginner_tutorials-msg:example instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <example>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-msg:data-val is deprecated.  Use beginner_tutorials-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <example>) ostream)
  "Serializes a message object of type '<example>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <example>) istream)
  "Deserializes a message object of type '<example>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'data) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<example>)))
  "Returns string type for a message object of type '<example>"
  "beginner_tutorials/example")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'example)))
  "Returns string type for a message object of type 'example"
  "beginner_tutorials/example")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<example>)))
  "Returns md5sum for a message object of type '<example>"
  "fdb28210bfa9d7c91146260178d9a584")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'example)))
  "Returns md5sum for a message object of type 'example"
  "fdb28210bfa9d7c91146260178d9a584")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<example>)))
  "Returns full string definition for message of type '<example>"
  (cl:format cl:nil "float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'example)))
  "Returns full string definition for message of type 'example"
  (cl:format cl:nil "float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <example>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <example>))
  "Converts a ROS message object to a list"
  (cl:list 'example
    (cl:cons ':data (data msg))
))
