# -*- encoding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class GlobalTestOpenAcademySession(TransactionCase):
    '''
    This create global test to sessions
    '''

    #Seudo-constructor method
    def setUp(self):
        super(GlobalTestOpenAcademySession, self).setUp()
        self.session = self.env['openacademy.session']
        self.partner_absa = self.env.ref('base.partner_admin')
        self.course = self.env.ref('openacademy.course1')

    #Generic methods

    #TEst methods
    def test_10_instructor_is_attendee(self):
        '''
        Check that raise of 'A session's instructor can't be an attendee'
        '''
        with self.assertRaisesRegexp(
                    ValidationError,
                    "++++ A session's instructor can't be an attendee ****"
                ):
                self.session.create({
                    'name':'Session test 1',
                    'seats': 1,
                    'instructor_id': self.partner_absa.id,
                    'attendee_ids': [(6,0, [self.partner_absa.id])],
                    'course_id': self.course.id,
                })

