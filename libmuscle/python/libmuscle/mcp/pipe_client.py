from typing import cast
from ymmsl import Reference

from libmuscle.mcp.client import Client
from libmuscle.mcp.message import Message
import libmuscle.mcp.pipe_multiplexer as mux


class PipeClient(Client):
    """A client for pipe-based communication.
    """
    @staticmethod
    def can_connect_to(location: str) -> bool:
        """Whether this client class can connect to the given location.

        Args:
            location: The location to potentially connect to.

        Returns:
            True iff this class can connect to this location.
        """
        return mux.can_connect_to(location)

    @staticmethod
    def shutdown(instance_id: Reference) -> None:
        """Free any resources shared by all clients for this instance.
        """
        if mux.can_communicate_for(instance_id):
            _, mux_client_conn = mux.get_pipes_for_instance(instance_id)
            mux_client_conn.close()

    def __init__(self, instance_id: Reference, location: str) -> None:
        """Creates a PipeClient.

        Args:
            instance_id: Our instance id.
            peer_id: Id of the peer (server) we're connecting to.
        """
        self._instance_id = instance_id

        _, mux_client_conn = mux.get_pipes_for_instance(instance_id)
        _, peer_id = location.split('/')

        # request connection
        mux_client_conn.send(peer_id)
        self._conn = mux_client_conn.recv()

    def receive(self, receiver: Reference) -> Message:
        """Receive a message from a port this client connects to.

        Args:
            receiver: The receiving (local) port.

        Returns:
            The received message.
        """
        self._conn.send(receiver)
        return cast(Message, self._conn.recv())

    def close(self) -> None:
        """Closes this client.

        This closes any connections this client has and/or performs
        other shutdown activities.
        """
        self._conn.close()