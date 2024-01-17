;; Auto-generated. Do not edit!


(when (boundp 'final_rover::encodersFeedback)
  (if (not (find-package "FINAL_ROVER"))
    (make-package "FINAL_ROVER"))
  (shadow 'encodersFeedback (find-package "FINAL_ROVER")))
(unless (find-package "FINAL_ROVER::ENCODERSFEEDBACK")
  (make-package "FINAL_ROVER::ENCODERSFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude encodersFeedback.msg.html


(defclass final_rover::encodersFeedback
  :super ros::object
  :slots (_first _second ))

(defmethod final_rover::encodersFeedback
  (:init
   (&key
    ((:first __first) 0.0)
    ((:second __second) 0.0)
    )
   (send-super :init)
   (setq _first (float __first))
   (setq _second (float __second))
   self)
  (:first
   (&optional __first)
   (if __first (setq _first __first)) _first)
  (:second
   (&optional __second)
   (if __second (setq _second __second)) _second)
  (:serialization-length
   ()
   (+
    ;; float64 _first
    8
    ;; float64 _second
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _first
       (sys::poke _first (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _second
       (sys::poke _second (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _first
     (setq _first (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _second
     (setq _second (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get final_rover::encodersFeedback :md5sum-) "c8951f7da38088f2e93267537583f4e8")
(setf (get final_rover::encodersFeedback :datatype-) "final_rover/encodersFeedback")
(setf (get final_rover::encodersFeedback :definition-)
      "float64 first
float64 second
")



(provide :final_rover/encodersFeedback "c8951f7da38088f2e93267537583f4e8")


