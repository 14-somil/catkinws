
(cl:in-package :asdf)

(defsystem "final_rover-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "GPS" :depends-on ("_package_GPS"))
    (:file "_package_GPS" :depends-on ("_package"))
    (:file "RoverMsg" :depends-on ("_package_RoverMsg"))
    (:file "_package_RoverMsg" :depends-on ("_package"))
    (:file "anglesMsg" :depends-on ("_package_anglesMsg"))
    (:file "_package_anglesMsg" :depends-on ("_package"))
    (:file "armClient" :depends-on ("_package_armClient"))
    (:file "_package_armClient" :depends-on ("_package"))
    (:file "encodersFeedback" :depends-on ("_package_encodersFeedback"))
    (:file "_package_encodersFeedback" :depends-on ("_package"))
    (:file "roverServer" :depends-on ("_package_roverServer"))
    (:file "_package_roverServer" :depends-on ("_package"))
  ))