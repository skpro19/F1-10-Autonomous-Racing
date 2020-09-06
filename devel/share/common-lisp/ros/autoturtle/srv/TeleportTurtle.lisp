; Auto-generated. Do not edit!


(cl:in-package autoturtle-srv)


;//! \htmlinclude TeleportTurtle-request.msg.html

(cl:defclass <TeleportTurtle-request> (roslisp-msg-protocol:ros-message)
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
   (theta
    :reader theta
    :initarg :theta
    :type cl:float
    :initform 0.0))
)

(cl:defclass TeleportTurtle-request (<TeleportTurtle-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TeleportTurtle-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TeleportTurtle-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name autoturtle-srv:<TeleportTurtle-request> is deprecated: use autoturtle-srv:TeleportTurtle-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <TeleportTurtle-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autoturtle-srv:x-val is deprecated.  Use autoturtle-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <TeleportTurtle-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autoturtle-srv:y-val is deprecated.  Use autoturtle-srv:y instead.")
  (y m))

(cl:ensure-generic-function 'theta-val :lambda-list '(m))
(cl:defmethod theta-val ((m <TeleportTurtle-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autoturtle-srv:theta-val is deprecated.  Use autoturtle-srv:theta instead.")
  (theta m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TeleportTurtle-request>) ostream)
  "Serializes a message object of type '<TeleportTurtle-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'theta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TeleportTurtle-request>) istream)
  "Deserializes a message object of type '<TeleportTurtle-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'theta) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TeleportTurtle-request>)))
  "Returns string type for a service object of type '<TeleportTurtle-request>"
  "autoturtle/TeleportTurtleRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TeleportTurtle-request)))
  "Returns string type for a service object of type 'TeleportTurtle-request"
  "autoturtle/TeleportTurtleRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TeleportTurtle-request>)))
  "Returns md5sum for a message object of type '<TeleportTurtle-request>"
  "a130bc60ee6513855dc62ea83fcc5b20")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TeleportTurtle-request)))
  "Returns md5sum for a message object of type 'TeleportTurtle-request"
  "a130bc60ee6513855dc62ea83fcc5b20")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TeleportTurtle-request>)))
  "Returns full string definition for message of type '<TeleportTurtle-request>"
  (cl:format cl:nil "float32 x~%float32 y~%float32 theta~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TeleportTurtle-request)))
  "Returns full string definition for message of type 'TeleportTurtle-request"
  (cl:format cl:nil "float32 x~%float32 y~%float32 theta~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TeleportTurtle-request>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TeleportTurtle-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TeleportTurtle-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':theta (theta msg))
))
;//! \htmlinclude TeleportTurtle-response.msg.html

(cl:defclass <TeleportTurtle-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass TeleportTurtle-response (<TeleportTurtle-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TeleportTurtle-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TeleportTurtle-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name autoturtle-srv:<TeleportTurtle-response> is deprecated: use autoturtle-srv:TeleportTurtle-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TeleportTurtle-response>) ostream)
  "Serializes a message object of type '<TeleportTurtle-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TeleportTurtle-response>) istream)
  "Deserializes a message object of type '<TeleportTurtle-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TeleportTurtle-response>)))
  "Returns string type for a service object of type '<TeleportTurtle-response>"
  "autoturtle/TeleportTurtleResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TeleportTurtle-response)))
  "Returns string type for a service object of type 'TeleportTurtle-response"
  "autoturtle/TeleportTurtleResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TeleportTurtle-response>)))
  "Returns md5sum for a message object of type '<TeleportTurtle-response>"
  "a130bc60ee6513855dc62ea83fcc5b20")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TeleportTurtle-response)))
  "Returns md5sum for a message object of type 'TeleportTurtle-response"
  "a130bc60ee6513855dc62ea83fcc5b20")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TeleportTurtle-response>)))
  "Returns full string definition for message of type '<TeleportTurtle-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TeleportTurtle-response)))
  "Returns full string definition for message of type 'TeleportTurtle-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TeleportTurtle-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TeleportTurtle-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TeleportTurtle-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TeleportTurtle)))
  'TeleportTurtle-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TeleportTurtle)))
  'TeleportTurtle-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TeleportTurtle)))
  "Returns string type for a service object of type '<TeleportTurtle>"
  "autoturtle/TeleportTurtle")