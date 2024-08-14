from http.server import *
import http.client as cli
import requests
import device_management_pb2
import socket
class A(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        dat = self.rfile.read(int(self.headers.get('Content-Length')))
        dmr = device_management_pb2.DeviceManagementRequest()
        dmr.ParseFromString(dat)
        print(dmr)
        if (dmr.device_state_retrieval_request):
            # Expecting a device state response
            x = device_management_pb2.DeviceManagementResponse()
            rr = device_management_pb2.DeviceStateRetrievalResponse()
            dv = device_management_pb2.DeviceInitialEnrollmentStateResponse()
            dv.Clear()
            dv.initial_enrollment_mode = 0
            dv.management_domain = ""
            dv.is_license_packaged_with_device = False
            dv.disabled_state = False
            rr.initial_state_response = dv
            rr.restore_mode = 0
            rr.management_domain = ""
            self.wfile.write(rr.SerializeToString())
            return
            
        
        print("data read")
        print(dat)
        con = requests.request('POST', 'https://m.google.com/devicemanagement/data/api', data=dat, headers=dict(self.headers))
        self.wfile.write(bytes(str(con.status_code), 'utf-8'))
        # self.wfile.close()
hs = HTTPServer(("0.0.0.0", 3040), A)
hs.serve_forever()
