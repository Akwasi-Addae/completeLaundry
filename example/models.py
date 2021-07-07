from django.db import models
import socket

class Company(models.Model):
    name = models.CharField(max_length=20)
    address = "192.168.0.12"
    port = 9000

    def server(self):
        server_sock = socket.socket()
        server_sock.bind((self.address,self.port))
        self.status = "Listening on port"
        server_sock.listen(2)

        conn, addr = server_sock.accept()
        self.status = ("Accepted connection from", addr)


class farRockaway(models.Model):
    washerName = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.washerName
