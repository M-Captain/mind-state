from .community import COMMUNITY_MEMBERS


def community_members(_request):
    return {"community_members": COMMUNITY_MEMBERS}
