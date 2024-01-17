;; Auto-generated. Do not edit!


(when (boundp 'final_rover::armClient)
  (if (not (find-package "FINAL_ROVER"))
    (make-package "FINAL_ROVER"))
  (shadow 'armClient (find-package "FINAL_ROVER")))
(unless (find-package "FINAL_ROVER::ARMCLIENT")
  (make-package "FINAL_ROVER::ARMCLIENT"))

(in-package "ROS")
;;//! \htmlinclude armClient.msg.html


(defclass final_rover::armClient
  :super ros::object
  :slots (_y _command _position _pitch _yaw _gripper ))

(defmethod final_rover::armClient
  (:init
   (&key
    ((:y __y) 0.0)
    ((:command __command) 0)
    ((:position __position) 0)
    ((:pitch __pitch) 0.0)
    ((:yaw __yaw) 0.0)
    ((:gripper __gripper) 0)
    )
   (send-super :init)
   (setq _y (float __y))
   (setq _command (round __command))
   (setq _position (round __position))
   (setq _pitch (float __pitch))
   (setq _yaw (float __yaw))
   (setq _gripper (round __gripper))
   self)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:position
   (&optional __position)
   (if __position (setq _position __position)) _position)
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:gripper
   (&optional __gripper)
   (if __gripper (setq _gripper __gripper)) _gripper)
  (:serialization-length
   ()
   (+
    ;; float64 _y
    8
    ;; char _command
    1
    ;; int16 _position
    2
    ;; float64 _pitch
    8
    ;; float64 _yaw
    8
    ;; int16 _gripper
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; char _command
       (write-byte _command s)
     ;; int16 _position
       (write-word _position s)
     ;; float64 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int16 _gripper
       (write-word _gripper s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; char _command
     (setq _command (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; int16 _position
     (setq _position (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float64 _pitch
     (setq _pitch (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw
     (setq _yaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int16 _gripper
     (setq _gripper (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get final_rover::armClient :md5sum-) "6475c3b95c87883ceb5174259fc15e38")
(setf (get final_rover::armClient :datatype-) "final_rover/armClient")
(setf (get final_rover::armClient :definition-)
      "float64 y
char command
int16 position
float64 pitch
float64 yaw
int16 gripper
")



(provide :final_rover/armClient "6475c3b95c87883ceb5174259fc15e38")


