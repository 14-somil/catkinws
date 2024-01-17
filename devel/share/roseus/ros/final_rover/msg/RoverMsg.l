;; Auto-generated. Do not edit!


(when (boundp 'final_rover::RoverMsg)
  (if (not (find-package "FINAL_ROVER"))
    (make-package "FINAL_ROVER"))
  (shadow 'RoverMsg (find-package "FINAL_ROVER")))
(unless (find-package "FINAL_ROVER::ROVERMSG")
  (make-package "FINAL_ROVER::ROVERMSG"))

(in-package "ROS")
;;//! \htmlinclude RoverMsg.msg.html


(defclass final_rover::RoverMsg
  :super ros::object
  :slots (_x _y _isPID ))

(defmethod final_rover::RoverMsg
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:isPID __isPID) nil)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _isPID __isPID)
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:isPID
   (&optional (__isPID :null))
   (if (not (eq __isPID :null)) (setq _isPID __isPID)) _isPID)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; bool _isPID
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _isPID
       (if _isPID (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _isPID
     (setq _isPID (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get final_rover::RoverMsg :md5sum-) "dac2c668a77a0aca11621addd50fbbe9")
(setf (get final_rover::RoverMsg :datatype-) "final_rover/RoverMsg")
(setf (get final_rover::RoverMsg :definition-)
      "float64 x
float64 y
bool isPID
")



(provide :final_rover/RoverMsg "dac2c668a77a0aca11621addd50fbbe9")


