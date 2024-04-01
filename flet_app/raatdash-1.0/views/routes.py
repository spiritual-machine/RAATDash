from views.router import Router, DataStrategyEnum
from views.login import Login
from views.register import Register
router = Router(DataStrategyEnum.QUERY)

router.routes = {
  "/login": Login,
  "/register": Register
}