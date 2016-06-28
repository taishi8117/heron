# Copyright 2016 Twitter. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#import unittest2 as unittest
import socket
import unittest
from heron.instance.src.python.network.protocol import REQID, HeronProtocol, IncomingPacket
import mock_generator

class ProtocolTest(unittest.TestCase):
  def setUp(self):
    pass

  def test_reqid(self):
    reqid = REQID.generate()
    packed_reqid = REQID.pack(reqid)
    unpacked_reqid = REQID.unpack(packed_reqid)

    self.assertEqual(reqid, unpacked_reqid)

    zero_reqid = REQID.generate_zero()
    packed_zero = REQID.pack(zero_reqid)
    # the length of REQID is 32 bytes
    self.assertEqual(packed_zero, bytearray(0 for i in range (32)))

  def test_encode_decode_packet(self):
    # get_mock_packets() uses HeronProtocol.get_outgoing_packet
    pkt_list, raw_list = mock_generator.get_mock_packets()
    for pkt, raw in zip(pkt_list, raw_list):
      raw_reqid, raw_message = raw
      typename, reqid, seriazelid_msg = HeronProtocol.decode_packet(pkt)
      self.assertEqual(reqid, raw_reqid)
      self.assertEqual(typename,raw_message.DESCRIPTOR.full_name)
      self.assertEqual(seriazelid_msg, raw_message.SerializeToString())

  def test_fail_decode_packet(self):
    packet = mock_generator.get_fail_packet()
    with self.assertRaises(RuntimeError):
      HeronProtocol.decode_packet(packet)

  def test_read(self):
    normal_dispatcher = mock_generator.MockDispatcher()
    normal_dispatcher.prepare_normal()
    pkt = IncomingPacket()
    pkt.read(normal_dispatcher)
    self.assertTrue(pkt.is_header_read)
    self.assertTrue(pkt.is_complete)

    header_dispatcher = mock_generator.MockDispatcher()
    header_dispatcher.prepare_header_only()
    pkt = IncomingPacket()
    pkt.read(header_dispatcher)
    self.assertTrue(pkt.is_header_read)
    self.assertFalse(pkt.is_complete)
    self.assertEqual(pkt.data, "")

    partial_data_dispatcher = mock_generator.MockDispatcher()
    partial_data_dispatcher.prepare_partial_data()
    pkt = IncomingPacket()
    pkt.read(partial_data_dispatcher)
    self.assertTrue(pkt.is_header_read)
    self.assertFalse(pkt.is_complete)
    self.assertEqual(len(pkt.data), partial_data_dispatcher.PARTIAL_DATA_SIZE)

    try:
      eagain_dispatcher = mock_generator.MockDispatcher()
      eagain_dispatcher.prepare_eagain()
      pkt = IncomingPacket()
      pkt.read(eagain_dispatcher)
    except Exception:
      self.fail("Exception raised unexpectedly when testing EAGAIN error")

    with self.assertRaises(RuntimeError):
      fatal_dispatcher = mock_generator.MockDispatcher()
      fatal_dispatcher.prepare_fatal()
      pkt = IncomingPacket()
      pkt.read(fatal_dispatcher)




