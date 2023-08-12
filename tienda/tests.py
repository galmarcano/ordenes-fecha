from django.test import TestCase
from tienda.models import Orden
from datetime import datetime
from django.utils import timezone
import zoneinfo
# Create your tests here.
class TiendaViewsTests(TestCase):
    def test_v_index(self):
        #Debe entregar todos los registros si no existen filtros

        respuesta = self.client.get("/")

        ords = respuesta.context["ordenes"]

        self.assertEqual(0, len(ords))

        new = Orden()
        new.cliente = 'Jaimito'
        new.fecha = '2023-05-06'
        new.fecha_envio= '2023-05-18'
        new.direccion = 'La florida'
        new.save()

        respuesta = self.client.get("/")

        ords = respuesta.context["ordenes"]

        self.assertEqual(1, len(ords))

    def test_v_index_filtros(self):
        #entrega los registros con filtros de fecha

        new = Orden()
        new.cliente = 'Jose'
        new.fecha = '2022-05-06'
        new.fecha_envio= datetime(2022, 5, 8).\
            astimezone(zoneinfo.ZoneInfo('America/Santiago'))
        new.direccion = 'La florida'
        new.save()

        new = Orden()
        new.cliente = 'Pascal'
        new.fecha = '2023-05-06'
        new.fecha_envio= datetime(2023, 5, 8).\
            astimezone(zoneinfo.ZoneInfo('America/Santiago'))
        new.direccion = 'La florida'
        new.save()

        res = self.client.get('/?fecha_inicio=%s&fecha_fin=%s' % (
            '2023-05-06',
            '2023-05-25'
        ))

        ords = res.context["ordenes"]

        self.assertEqual(1, len(ords))


