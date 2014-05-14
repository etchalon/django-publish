class DetectDraftMode(object):
    def process_request(self, request):
        if 'draft' in request.GET:
            request.is_draft = True
        else:
            request.is_draft = False