# importing all from ctypes
from ctypes import Structure, c_ubyte, c_ushort, c_uint32

from ctypes import *
# Importing libraries
import socket
import struct


class IP(Structure):
    _fields_ = [
        ("ihl", c_ubyte, 4),           #4 bit unsigned char.
        ("version", c_ubyte, 4),       #4 bit unsigned char.
        ("tos", c_ubyte, 8),           #1 Byte char.
        ("len", c_ushort, 16),         #2 byte unsigned short.
        ("id", c_ushort, 16),          #2 byte unsigned short.
        ("offset", c_ushort, 16),      #2 byte unsigned short.
        ("ttl", c_ubyte, 8),           #1 byte char.
        ("protocol_num", c_ubyte, 8),  #1 byte char.
        ("sum", c_ushort, 8),          #2 byte unsigned short.
        ("src", c_uint32, 32),         #4 byte unsigned int.
        ("dst", c_uint32, 32)          #4 byte unsigned int.
    ]
    def __new__(cls, socket_buffer=None):
        """
        Creating a method that creates a new buffer.
        :param socket_buffer:
        """
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        """
        Initializing the main method with an init.
        :param socket_buffer:
        """
        #Human readable IP addresses
        self.socket_buffer = socket_buffer
        self.src_address = socket.inet_ntoa(struct.pack("<L",self.src))
        self.src_address = socket.inet_ntoa(struct.pack("<L",self.dst))


class Structure:
    pass


def c_ubyte():
    return None


def c_ushort():
    return None


def c_uint32():
    return None