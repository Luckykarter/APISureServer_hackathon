from rest_framework.decorators import api_view
from rest_framework.response import Response
from APISureConnector.apisureconnector import APISureConnector
from apisure.models import Guarantee, Project
from .serializers import GuaranteeSerializer, ProjectSerializer
from pprint import pp

CONNECTOR = APISureConnector(client_id="gAtxkHbIAwDOHnSTajn0p0tN4V6Yhk1B",
                             client_secret="80OdKmebSkWlpkGP")


@api_view(["GET"])
def get_guarantee(request, **kwargs):
    deal_number = kwargs.get("deal_number")
    if deal_number:
        deals = Guarantee.objects.filter(dealNumber=deal_number)
    else:
        deals = Guarantee.objects.all()

    serializer = GuaranteeSerializer(deals, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def send_guarantee(request, **kwargs):
    url = 'https://api.apisure.io/mapi_base/v1/Guarantee/Guarantee/Apply'

    response = CONNECTOR.send_request(url=url, data=request.data)
    print(response)
    pp(response.json())

    if response.status_code == 200:

        guarantee = None
        try:
            info_bar = response.json().get("data").get("infoBar")
            guarantee = Guarantee()
            guarantee.add_entry(info_bar)
            print(request.data)
            guarantee.set_amount(request.data)
        except:
            pass
        finally:
            if guarantee is not None:
                guarantee.save()

    return Response(response.json(), status=response.status_code)


@api_view(['POST'])
def test_guarantee(request, **kwargs):
    guarantee = Guarantee()
    guarantee.deal_number = "test"
    guarantee.amount = 123.55
    guarantee.save()

    return Response(status=200)


@api_view(['POST', 'GET'])
def post_project(request, **kwargs):
    if request.method == 'POST':
        Project.objects.create(**request.data)
        return Response(status=200)
    else:
        projects = Project.objects.all().order_by('-id')
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
